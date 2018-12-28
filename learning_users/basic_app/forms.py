from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

# UserForm is uses fields already defined through the django user model
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        # fields from the user model that we want incorporated into the form
        fields = ('username', 'email', 'password')

# UserProfileInfoForm contains the new fields we wish to add onto the form
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
