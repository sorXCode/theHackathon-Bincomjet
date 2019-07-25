from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import *

def profile_create(request):
    if request.method == 'GET':
        form = ProfilecreateForm(request.POST)
    return render(request, 'testing_apis/testing.html', {'form': form})

def profile_update(request):
    if request.method == 'GET':
        form = ProfileupdateForm(request.POST)
    return render(request, 'testing_apis/testing1.html', {'form': form})

def profile_login(request):
    if request.method == 'GET':
        form = LoginForm(request.POST)
    return render(request, 'testing_apis/testing12.html', {'form': form})

def profile_view(request):
    if request.method == 'GET':
        form = ProfileviewForm(request.POST)
    return render(request, 'testing_apis/testing13.html', {'form': form})

def bankdetails(request):
    if request.method == 'GET':
        form = UserbankDetailsForm(request.POST)
    return render(request, 'testing_apis/testing2.html', {'form': form})

def companydetails(request):
    if request.method == 'GET':
        form = UserworkDetailsForm(request.POST)
    return render(request, 'testing_apis/testing3.html', {'form': form})

def motor(request):
    if request.method == 'GET':
        form = MotorInsuranceForm(request.POST)
    return render(request, 'testing_apis/testing4.html', {'form': form})

def author(request):
    if request.method == 'GET':
        form = AuthorForm(request.POST)
    return render(request, 'testing_apis/testing5.html', {'form': form})