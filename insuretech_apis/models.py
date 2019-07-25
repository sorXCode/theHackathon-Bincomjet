from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import keygenv1 as kv

class AInsuranceUserProfile (models.Model):
    def __init__(self,*args,**kwargs):
        models.Model.__init__(self,*args,**kwargs)

    username = models.CharField(max_length=100, blank=False, default='')
    password = models.CharField(max_length=100, blank=False, default='')
    firstname = models.CharField(max_length=100, blank=False, default='')
    lastname = models.CharField(max_length=100, blank=False, default='')
    email = models.EmailField(blank=True, default='')
    registrationdate = models.DateTimeField(auto_now_add=True)
    image = models.URLField(blank=True, default='')
    token = models.CharField(max_length=100, default=str(kv.main(4,12)),)
    def __str__(self):
        return self.username



@receiver(post_save, sender=AInsuranceUserProfile)
def save_password(sender, instance, **kwargs):
    if kwargs['created']:
        pass
    else:
        pass

class AUserbankDetails (models.Model):
    insuranceuserprofile = models.ForeignKey(AInsuranceUserProfile, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=100, blank=True, default='')
    account_name = models.CharField(max_length=100, blank=True, default='')
    account_number = models.IntegerField(blank=True, default=0)
    bvn = models.IntegerField(blank=True, default=0)
    phone_number = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.account_name


class AUserworkDetails (models.Model):
    insuranceuserprofile = models.ForeignKey(AInsuranceUserProfile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True, default='')
    role = models.CharField(max_length=100, blank=True, default='')
    def __str__(self):
        return self.company_name


class AMotorInsurance (models.Model):
    GOODS_CHOICE = (('General_cartage', 'General_cartage'),
                        ('Goods_only', 'Goods_only'),
                        ('Passangers_only', 'Passangers_only'),)
    insuranceuserprofile = models.ForeignKey(AInsuranceUserProfile, on_delete=models.CASCADE)
    avg_maintenance = models.CharField(max_length=100, blank=True, default='')
    chassis_number = models.CharField(max_length=100, blank=True, default='')
    cost_price = models.IntegerField(blank=True, default=0)
    date_of_purchase = models.DateTimeField(auto_now_add=True)
    engine_number = models.IntegerField(blank=True, default=0)
    fuel_capacity = models.IntegerField(blank=True, default=0)
    mileage = models.IntegerField(blank=True, default=0)
    car_model = models.CharField(max_length=100, blank=True, default='')
    car_use = models.CharField(choices=GOODS_CHOICE,max_length=100, default='General_cartage')
    purpose = models.CharField(max_length=100, blank=True, default='')
    reg_no = models.IntegerField(blank=True, default=0)
    vehicle_faults = models.TextField(blank=True, default='')
    vehicle_types = models.CharField(max_length=100, blank=True, default='')
    def __str__(self):
        return self.insuranceuserprofile



class Author(models.Model):
    created = models.DateTimeField(auto_now_add=False)
    username = models.CharField(max_length=100, blank=True, default='')
    linenos = models.BooleanField(default=False)

    def __str__(self):
        return self.username

