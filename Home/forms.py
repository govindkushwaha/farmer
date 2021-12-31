from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from Home.models import farmer, buyer,Farmerupload,ContactUs
from django.forms import ModelForm

class FarmeruploadForm(forms.ModelForm):
     
     class Meta:
        model = Farmerupload
        fields = ['Image','Name','contact','Address','state_country','city_dist','Occupation', 'ProduceName','Email','TotQuantity','Quality','Category','Price_Kg' ]

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['Name','Email','contact','message']