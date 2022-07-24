from django.http import HttpResponse, JsonResponse
from store.models import Coffee, Profile, Category, Address, Order
from store.serializers import CoffeeSerializer, CategorySerializer, ProfileSerializer, UserSerializer, AddressSerializer, UserSerializerAuthenticate, UserSerializerRegister, OrderSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class OrderDetail(generics.GenericAPIView):

    serializer_class = OrderSerializer

    def get(self, request, pk, format=None):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk):
        data = request.data
        order = Order.objects.get(pk=pk)

        order.products.clear()
        order.save()

        address = request.data["address"]
        address_id = address['id']

        address_obj = Address.objects.get(pk=address_id)
        order.address = address_obj
        

        for product in data["products"]:
            product_obj = Coffee.objects.get(pk=product['id'])
            order.products.add(product_obj)
        
        
        serializer = OrderSerializer(order)
        
        return Response(serializer.data)



class OrderList(generics.GenericAPIView):

    serializer_class = OrderSerializer

    def get(self, request, format=None):

        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        new_order = Order.objects.create()
        new_order.save()

        address = request.data["address"]
        address_id = address['id']

        address_obj = Address.objects.get(pk=address_id)
        new_order.address = address_obj

        for product in data["products"]:
            product_obj = Coffee.objects.get(pk=product['id'])
            new_order.products.add(product_obj)
        
        
        serializer = OrderSerializer(new_order)
        
        return Response(serializer.data)

class AddressDetail(generics.GenericAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def put(self, request, pk):
        address = Address.objects.get(pk=pk)
        address.name = request.data["name"]
        address.street = request.data["street"]
        address.city = request.data["street"]
        address.country = request.data["country"]
        address.number = request.data["number"]

        serializer = AddressSerializer(address)
        address.save()
        return Response(serializer.data)
   
        
class AddressList(generics.GenericAPIView):

    serializer_class = AddressSerializer
   

    def get(self, request, format=None):

        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

    def post(self, request):
    
        address = AddressSerializer(data=request.data)

        if address.is_valid():
            address.save()
            return Response(address.data, status=status.HTTP_201_CREATED)
        return Response(address.data, status.HTTP_400_BAD_REQUEST)


class Authenticate(generics.GenericAPIView):

    serializer_class = UserSerializerAuthenticate

    def post(self, request):

        return null

class Register(generics.GenericAPIView):

    serializer_class = UserSerializerRegister

    def post(self, request):
        data = request.data
        user = User.objects.create_user(username=data['username'],
                                        email=data['email'],
                                        password=data['password'])
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class CoffeeList(generics.GenericAPIView):

    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer
   
    def get(self, request, format=None):
        coffees = Coffee.objects.all()
        serializer = CoffeeSerializer(coffees, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        new_coffee = Coffee.objects.create(name=data["name"], description=data["description"], price=data["price"])

        new_coffee.save()

        for category in data["categories"]:
            category_obj = Category.objects.get(pk=category["id"])
            new_coffee.categories.add(category_obj)

        serializer = CoffeeSerializer(new_coffee)

        return Response(serializer.data)
        
        

class CategoryFilterSet(django_filters.FilterSet):    
    class Meta:
        model = Category
        fields = ['name']

class CategoryList(generics.GenericAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = CategoryFilterSet
    filterset_fields = ['name']

    def get(self, request):
        queryset = Category.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        serializer = CategorySerializer(queryset, many=True)
       
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
class ProfileAddress(generics.GenericAPIView):
    def get(self, request, pk):
        profile = Profile.objects.get(pk=pk)
        address = profile.address_set.all()

        serializer = AddressSerializer(address, many=True)
       
        return Response(serializer.data) 
      

class ProfileDetail(generics.GenericAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        profile = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


    def put(self, request, pk):
        data = request.data
        profile = Profile.objects.get(pk=pk)

        profile.taxNumber = data["taxNumber"]
        profile.birth_date = data["birth_date"]

        profile.address_set.clear()
        profile.save()

        for address in data["address_set"]:
            address_obj = Address.objects.get(pk=address)
            profile.address_set.add(address_obj)
        
        
        serializer = ProfileSerializer(profile)
        
        return Response(serializer.data)
          

class ProfileList(generics.GenericAPIView):

    def get(self, request):
        queryset = Profile.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(username=username)
        serializer = ProfileSerializer(queryset, many=True)
       
        return Response(serializer.data)

    
   

    

