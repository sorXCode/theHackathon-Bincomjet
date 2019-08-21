from django import forms
from django.forms import ModelForm
from .models import *

class LoginForm(ModelForm):
    class Meta:
        model = InsuranceUserProfile
        fields = ['username','password']

class ProfilecreateForm(ModelForm):
    class Meta:
        model = InsuranceUserProfile
        fields = ['username','password']

class ProfileviewForm(ModelForm):
    class Meta:
        model = InsuranceUserProfile
        fields = ['token',]

class ProfileupdateForm(ModelForm):
    class Meta:
        model = InsuranceUserProfile
        exclude = ['registrationdate']

class UserbankDetailsForm(ModelForm):
    class Meta:
        model = UserbankDetails
        exclude = ['insuranceuserprofile',]


class UserworkDetailsForm(ModelForm):
    class Meta:
        model = UserworkDetails
        exclude = ['insuranceuserprofile',]

class MotorInsuranceForm(ModelForm):
    class Meta:
        model = MotorInsurance
        exclude = ['insuranceuserprofile',]

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'