from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class extendedfarmer(models.Model):
    Phonenumber = models.CharField(max_length=50)
    Address = models.CharField(max_length = 50)
    state=models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
