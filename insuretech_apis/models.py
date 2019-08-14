from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import keygenv1 as kv
import string
import random

class Ap():
    @classmethod
    def toks(cls, a, b):
        SEQ = string.ascii_uppercase + string.digits
        def shake(seq, n):
            randomstr = (','.join(random.choice(seq) for _ in range(n))).split(',')
            for i in range(n):
                random.shuffle(randomstr)
            return ''.join(randomstr)

        def main(pattern_no, str_len,):
            keygen2 = lambda: ''.join(shake(SEQ, pattern_no) for _ in range(str_len))
            return keygen2()

        return main(a, b)

    @classmethod
    def serviceid(cls, n1, n2, text):
        STRSEQ = string.ascii_uppercase
        NUMSEQ = string.digits
        def main(n1, n2 ,text,):
            str1=text
            str2 = (''.join(random.choice(STRSEQ) for _ in range(n1)))
            str3 = (''.join(random.choice(NUMSEQ) for _ in range(n2)))
            return (str1 + str2 + str3)

        return main(n1, n2,text)

class AInsuranceUserProfile (models.Model):
    def __init__(self,*args,**kwargs):
        models.Model.__init__(self,*args,**kwargs)

    username = models.CharField(max_length=100, blank=False, default='')
    password = models.CharField(max_length=100, blank=False, default='')
    firstname = models.CharField(max_length=100, blank=False, default='')
    lastname = models.CharField(max_length=100, blank=False, default='')
    email = models.EmailField(blank=True, default='')
    score = models.IntegerField(blank=False, default=0)
    balance = models.IntegerField(blank=False, default=0)
    premium_fee = models.IntegerField(blank=False, default=0)
    premium_status = models.BooleanField(default=False)
    image = models.URLField(blank=True, default='')
    token = models.CharField(max_length=100, blank=True, )
    registrationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email



@receiver(post_save, sender=AInsuranceUserProfile)
def save_token(sender, instance, **kwargs):
    if kwargs['created']:
        instance.token = Ap.toks(4,12)
        instance.save()

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
    cover_id = models.CharField(max_length=100, blank=True, )
    def __str__(self):
        return self.insuranceuserprofile.username

@receiver(post_save, sender=AMotorInsurance)
def save_cover_id(sender, instance, **kwargs):
    if kwargs['created']:
        instance.cover_id = Ap.serviceid(4,6,'MOTOR-')
        instance.save()

class MotorUpdateRecord(models.Model):
    insuranceuserprofile = models.ForeignKey(AInsuranceUserProfile, on_delete=models.CASCADE)
    paymentcover = models.ForeignKey(AMotorInsurance, on_delete=models.CASCADE)
    date_of_record = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=100, blank=True,)
    def __str__(self):
        return self.insuranceuserprofile.username

class PremiumMotor (models.Model):
    insuranceuserprofile = models.ForeignKey(AInsuranceUserProfile, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=True, default=0)
    paymentcover = models.OneToOneField(AMotorInsurance, on_delete=models.CASCADE)
    payment_status = models.BooleanField()
    date_of_paid = models.DateTimeField(auto_now_add=True)
    premium_id = models.CharField(max_length=100, blank=True, )
    def __str__(self):
        return self.insuranceuserprofile.username

@receiver(post_save, sender=PremiumMotor)
def save_premium_id(sender, instance, **kwargs):
    if kwargs['created']:
        instance.premium_id = Ap.serviceid(4,6,'PREMIUM-')
        instance.save()

class ClaimMotor (models.Model):
    CLAIM_CHOICE = (('Claim_Requested', 'Claim_Requested'),
                    ('ClaimEvaluation_in_Progress', 'ClaimEvaluation_in_Progress'),
                    ('Claim_Denied', 'Claim_Denied'),
                    ('Claim_Granted', 'Claim_Granted'),
                    ('Claim_Disbursed', 'Claim_Disbursed'),)
    insuranceuserprofile = models.ForeignKey(AInsuranceUserProfile, on_delete=models.CASCADE)
    claimcover = models.OneToOneField(AMotorInsurance, on_delete=models.CASCADE)
    status = models.CharField(choices=CLAIM_CHOICE,max_length=100, default='Claim_Requested')
    date_of_claim = models.DateTimeField(auto_now_add=True)
    claim_id = models.CharField(max_length=100, blank=True, )
    def __str__(self):
        return self.insuranceuserprofile.username

@receiver(post_save, sender=ClaimMotor)
def save_claim_id(sender, instance, **kwargs):
    if kwargs['created']:
        instance.claim_id = Ap.serviceid(4,6,'CLAIM-')
        instance.save()

class PaymentReceipt (models.Model):
    GOODS_CHOICE = (('General_cartage', 'General_cartage'),
                        ('Goods_only', 'Goods_only'),
                        ('Passangers_only', 'Passangers_only'),)
    insuranceuserprofile = models.ForeignKey(AInsuranceUserProfile, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True, default='')
    amount = models.IntegerField(blank=True, default=0)
    date_of_purchase = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, blank=True, )
    def __str__(self):
        return self.insuranceuserprofile.username

@receiver(post_save, sender=PaymentReceipt)
def save_transaction_id(sender, instance, **kwargs):
    if kwargs['created']:
        instance.transaction_id = Ap.serviceid(4,6,'PAYMENT-')
        instance.save()

class CreditReceipt (models.Model):
    GOODS_CHOICE = (('General_cartage', 'General_cartage'),
                        ('Goods_only', 'Goods_only'),
                        ('Passangers_only', 'Passangers_only'),)
    insuranceuserprofile = models.ForeignKey(AInsuranceUserProfile, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True, default='')
    amount = models.IntegerField(blank=True, default=0)
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, blank=True, )
    def __str__(self):
        return self.insuranceuserprofile.username

@receiver(post_save, sender=CreditReceipt)
def save_transaction_id(sender, instance, **kwargs):
    if kwargs['created']:
        instance.transaction_id = Ap.serviceid(4,6,'CREDIT-')
        instance.save()



class Author(models.Model):
    created = models.DateTimeField(auto_now_add=False)
    username = models.CharField(max_length=100, blank=True, default='')
    linenos = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Tips(models.Model):
    insurance_choices = (("general", "General"),
                         ('auto', 'Auto'),
                         ('life', 'Life'),
                         ('health', 'Health'),)
    insurance_type = models.CharField(choices=insurance_choices,
                                      max_length=50,
                                      default='general')
    tip = models.TextField()

    class Meta:
        ordering = ('-insurance_type',)

    def __str__(self):
        return f"{self.insurance_type} => {self.tip}"

