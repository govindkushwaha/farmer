from django.db import models
from django.contrib.auth.models import User
import datetime
from accounts.models import extendedfarmer

# Create your models here.
#farmer database to insert the data into the table or retrive 
#the data alse from the databases tables 
class farmer(models.Model):
    ID = models.AutoField(primary_key=True)
    Phonenumber = models.CharField(max_length=50)
    Address = models.CharField(max_length = 50)
    state=models.CharField(max_length=20)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


    

#createing a sigunp data into the table for database record into them
#buyer data base 
class buyer(models.Model):
    ID = models.AutoField(primary_key=True)
    Email = models.CharField(max_length = 50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Occupation=models.CharField(max_length=30)
    Pass=models.CharField(max_length=30)
    CPass=models.CharField(max_length=30)
    Phonenumber = models.CharField(max_length=50)
    Address = models.CharField(max_length = 50)
    state=models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class  Farmerupload(models.Model):
    Image = models.ImageField(upload_to='static/img', blank=True)
    Name=models.CharField(max_length=20)
    contact=models.IntegerField()
    Address = models.CharField(max_length=30)
    city_dist=models.CharField(max_length=30)
    state_country = models.CharField(max_length=20)
    Occupation= models.CharField(max_length=20)
    ProduceName=models.CharField(max_length=50)
    Email= models.CharField(max_length=20)
    TotQuantity = models.CharField(max_length=20)
    Quality=models.CharField(max_length=20)
    Category=models.CharField(max_length=50)
    Price_Kg=models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.ProduceName

class  uploadFarmer(models.Model):
    Name=models.CharField(max_length=20)
    contact=models.IntegerField()
    Address = models.TextField()
    state_country = models.CharField(max_length=20)
    Occupation= models.CharField(max_length=20)
    ProduceName=models.CharField(max_length=50)
    Email= models.CharField(max_length=35)
    TotQuantity = models.CharField(max_length=20)
    Quality=models.CharField(max_length=20)
    Category=models.CharField(max_length=50)
    Price_Kg=models.IntegerField()
    
    def __str__(self):
        return self.Name

class ContactUs(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    contact=models.IntegerField()
    message=models.TextField()

    def __str__(self):
        return self.Name