"""insuretech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers
from django.conf.urls import url, include
from .serializers import *

'''urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]'''

router = routers.SimpleRouter()
router.register(r'generaltips', GeneralTipsViewSet)
router.register(r'autotips', AutoTipsViewSet)
router.register(r'lifetips', LifeTipsViewSet)
router.register(r'healthtips', HealthTipsViewSet)


urlpatterns = [
    path('ad/', views.odd),
    path('profile_view_api/', views.profile_api),
    path('profile_update_api/', views.profile_update_api),
    path('profile_create_api/', views.profile_create_api),
    path('profile_login_api/', views.profile_login_api),
    path('bankdetails_api/', views.bankdetails_api),
    path('companydetails_api/', views.companydetails_api),
    path('motor_api/', views.motor_api),
    path('author_api/', views.author_api),
    url(r'', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
