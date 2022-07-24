from django.urls import path
from store import views
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('authenticate/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authenticate/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('authenticate/register/', views.Register.as_view()),
    path('addresses/', views.AddressList.as_view()),
    path('addresses/<int:pk>', views.AddressDetail.as_view()),
    path('register/', views.Register.as_view()),
    path('coffees/', views.CoffeeList.as_view()),
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:pk>', views.OrderDetail.as_view()),
    path('categories/', views.CategoryList.as_view() ),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
    path('profiles/<int:pk>/address', views.ProfileAddress.as_view())
  
]