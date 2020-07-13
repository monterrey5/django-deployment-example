# CODE IN VIDEO 151 - PRACTICAL PART
# (IT DIFFERS A BIT FROM THEORETICAL PART BELOW)
# SEE MORE COMMENTS TO CODE IN THE CODE BELOW

from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


# # CODE IN VIDEO 149 - THEORETICAL PART

# from django import forms
# from basic_app.models import UserProfileInfo
#
# class UserProfileInfoForm(forms.ModelForm):
#     portfolio = forms.URLField(required=False)
#     picture = forms.URLImage(required=False)
#
#     class Meta():
#         model = UserProfileInfo
#         exclude = ("user",)
