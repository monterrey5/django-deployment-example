# CODE IN VIDEO 151 - PRACTICAL PART
# (IT DIFFERS A BIT FROM THEORETICAL PART BELOW)
# SEE MORE COMMENTS TO CODE IN THE CODE BELOW

from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self):
        return self.user.username




# # CODE IN VIDEO 149 - THEORETICAL PART
#
# from django.db import models
# from django.contrib.auth.models import User
#
# # Create your models here.
#
# class UserProfileInfo(models.Model):
#
#     # create relationship (DO NOT inherit from User!)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     # add additional attributes you want
#     # default ones are: username, email, password, first name, surname
#     portfolio = models.URLField(blank=True)
#     picture = models.ImageField(upload_to="profile_pics")
#
#     def __str__(self):
#         # build-in attribute of django.contrib.auth.models.User!
        # return self.user.username
