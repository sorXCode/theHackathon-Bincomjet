
from django.contrib import admin
from django.urls import path
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers
from django.conf.urls import url, include

router = routers.SimpleRouter()
router.register(r'generaltips', views.GeneralTipsViewSet)
router.register(r'autotips', views.AutoTipsViewSet)
router.register(r'lifetips', views.LifeTipsViewSet)
router.register(r'healthtips', views.HealthTipsViewSet)


urlpatterns = [
    url(r'', include(router.urls)),
    path('profile_view_api/', views.profile_api),
    path('profile_update_api/', views.profile_update_api),
    path('profile_create_api/', views.profile_create_api),
    path('profile_login_api/', views.profile_login_api),
    path('bankdetails_create_api/', views.bankdetails_create_api),
    path('bankdetails_view_api/', views.bankdetails_view_api),
    path('companydetails_create_api/', views.companydetails_create_api),
    path('companydetails_view_api/', views.companydetails_view_api),
    #motor insurance
    path('auto_insurance_create_api/', views.auto_insurance_create_api),
    path('auto_insurance_view_api/', views.auto_insurance_view_api),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
