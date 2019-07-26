from django.contrib import admin
from django.utils import timezone
from . import models


@admin.register(models.AInsuranceUserProfile)
class AInsuranceUserProfileAdmin(admin.ModelAdmin):
    # list view
    list_display = ['username', 'firstname', 'lastname', 'token']


@admin.register(models.AUserbankDetails)
class AUserbankDetailsAdmin(admin.ModelAdmin):
    # list view
    list_display = ['account_name', 'bank_name', 'account_number']


@admin.register(models.AUserworkDetails)
class AUserworkDetailsAdmin(admin.ModelAdmin):
    # list view
    list_display = ['company_name', 'role', ]


@admin.register(models.AMotorInsurance)
class AMotorInsuranceAdmin(admin.ModelAdmin):
    # list view
    list_display = ['chassis_number', 'date_of_purchase', 'cost_price']


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    # list view
    list_display = ['username', 'linenos', 'created']


@admin.register(models.Tips)
class TipsAdmin(admin.ModelAdmin):
    list_display = ['insurance_type', 'tip']
    search_fields = ['tip']
