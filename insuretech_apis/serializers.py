from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class AInsuranceUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AInsuranceUserProfile
        fields = '__all__'
        #exclude = ['token','registrationdate',]

class AUserbankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AUserbankDetails
        fields = ['insuranceuserprofile',]

class AUserworkDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AUserworkDetails
        fields = ['insuranceuserprofile',]

class AMotorInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMotorInsurance
        fields = '__all__'#['insuranceuserprofile',]
#MotorUpdateRecord
class MotorUpdateRecord(serializers.ModelSerializer):
    class Meta:
        model = MotorUpdateRecord
        fields = ['insuranceuserprofile',]

class PremiumMotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumMotor
        fields = ['insuranceuserprofile',]

class ClaimMotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimMotor
        fields = ['insuranceuserprofile',]

class PaymentReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentReceipt
        fields = ['insuranceuserprofile',]

class CreditReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditReceipt
        fields = ['insuranceuserprofile',]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [ 'username',  'linenos','created']
        
class TipsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tips
        fields = ['tip',]
