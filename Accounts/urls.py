
from django.contrib import admin
from django.urls import path
from . import views as v
urlpatterns = [
    
    path('category/<int:id>/',v.getByCategory,name='getByCategory'),
    path('register',v.addUser,name='addUser'),
    path('login',v.login_view,name='login_view'),
    path('logout',v.logout_view,name='logout_view'),
    path('searchproduct',v.search,name='search'),
    path('addToCart/<int:id>/',v.addToCart,name='addToCart'),
    path('getCartList',v.cartlist,name='cartlist'),
    path('getorderList/<int:id>/',v.getOrderList,name='myorder'),
]
