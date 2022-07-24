from rest_framework import serializers
from store.models import Coffee, Category, Profile, Address, Order
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CoffeeSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=False)

    class Meta:
        model = Coffee
        fields = ['id', 'name', 'description', 'categories', 'price']
        depth = 1

class AddressSerializer(serializers.ModelSerializer):
    #profile = ProfileSerializer(read_only=False)
    class Meta:
        model = Address
        fields = ['id', 'name', 'street', 'city', 'country', 'number']

class OrderSerializer(serializers.ModelSerializer):

    address = AddressSerializer(read_only=False)
    products = CoffeeSerializer(many=True, read_only=False)

    class Meta:
        model = Order
        fields = ['id', 'products', 'total_price', 'address']

class UserSerializerRegister(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class UserSerializerAuthenticate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']



class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=False)
    address_set = serializers.PrimaryKeyRelatedField(read_only=False, many=True, queryset = Address.objects.all())

    class Meta:
        model = Profile
        fields = '__all__'



