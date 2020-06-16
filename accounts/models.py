from django.db import models

from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    date_of_birth = models.DateField(blank=True,null=True)

    photo = models.ImageField(upload_to="users/%y/%m/%d",default="Default_avthar.png",blank=True,null=True)

    gender_choices = (("Male","Male"),("Female","Female"),("Other","Other"),("Not_specified","Not Specified"))

    gender = models.CharField(max_length=15,choices=gender_choices,default="Not_specified",blank=True,null=True)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return "Profile for user {}".format(self.user.username)
