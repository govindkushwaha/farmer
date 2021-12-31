from . import views
from django.urls import path

urlpatterns =[
    path('register', views.register, name="register"),
    path('register/', views.register, name="register"),
    path('login', views.login, name="login"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('registerbuyer/', views.registerbuyer, name="registerbuyer"),
    path('registerbuyer', views.registerbuyer, name="registerbuyer"),

path('checkUser',views.ShowBuyerorFarmerprofile,name='checkUser'),
path('checkUser/',views.ShowBuyerorFarmerprofile,name='checkUser'),

path('farmerProfile',views.farmerProfile,name='farmerProfile'),
path('farmerProfile/',views.farmerProfile,name='farmerProfile'),

path('buyerProfile',views.buyerProfile,name='buyerProfile'), 
path('buyerProfile/',views.buyerProfile,name='buyerProfile'), 

 path('SellForm/',views.SellForm),
 path('SellForm/',views.SellForm),
 
 path('BuyForm',views.BuyForm),
 path('BuyForm/',views.BuyForm),
]