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
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

'''urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]'''


urlpatterns = [
    path('profile_create', views.profile_create, name='profile_create'),
    path('profile_update', views.profile_update, name='profile_update'),
    path('profile_login', views.profile_login, name='profile_login'),
    path('profile_view', views.profile_view, name='profile_view'),
    path('bankdetails', views.bankdetails, name='bankdetails'),
    path('companydetails', views.companydetails, name='companydetails'),
    path('motor', views.motor, name='motor'),
    path('author', views.author, name='author'),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
