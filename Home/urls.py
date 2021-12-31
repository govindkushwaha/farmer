from django.urls import path
from . import views 

urlpatterns=[
 path('',views.HomePage, name="HomePage"),
 path('HomePage',views.HomePage, name="HomePage"),

 path('Services',views.ServicesUS,name='Services'),
 path('Services/',views.ServicesUS,name='Services'),

 path('searchProduces',views.searchProduces,name='searchProduces'),
 path('searchProduces/',views.searchProduces,name='searchProduces'),

 path('Help',views.HelpUS,name='Help'), 
 path('Help/',views.HelpUS,name='Help'), 
 
 path('Contact',views.ContactUS,name='Contact'),
 path('Contact/',views.ContactUS,name='Contact'),
 
 path('About',views.AboutUS,name='About'),
 path('About/',views.AboutUS,name='About'),

 path('upload',views.FarmerUpload,name='upload'),
 path('upload/',views.FarmerUpload,name='upload'),

 path('FarmerToBuyerList',views.DisplayToBuyerProduces,name='FarmerToBuyerList'),
 path('FarmerToBuyerList/',views.DisplayToBuyerProduces,name='FarmerToBuyerList'),
 
]


