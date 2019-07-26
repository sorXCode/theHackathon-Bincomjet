from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['POST',])
def profile_update_api(request):
    try:
        token = request.data.copy().get('token') if not request.POST else request.POST.copy().get('token')
        snippets = AInsuranceUserProfile.objects.get(token=token)
    except AInsuranceUserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        serializer = AInsuranceUserProfileSerializer(snippets, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST',])
def profile_api(request):
    try:
        token = request.data.copy().get('token') if not request.POST else request.POST.copy().get('token')
        snippets = AInsuranceUserProfile.objects.get(token=token)
        print('success')
    except AInsuranceUserProfile.DoesNotExist:
        print('failed')
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        serializer = AInsuranceUserProfileSerializer(snippets,data=request.data)
        if serializer.is_valid():
            #serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST',])
def profile_login_api(request):
    #works
    try:
        token = request.data.copy().get('token') if not request.POST else request.POST.copy().get('token')
        snippets = AInsuranceUserProfile.objects.get(username=token)
    except AInsuranceUserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        serializer = ProfileLoginSerializer(snippets)
        return Response(serializer.data,)

@csrf_exempt
@api_view(['POST',])
def profile_create_api(request):
    if request.method == 'POST':
        #works
        serializer = AInsuranceUserProfileSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def bankdetails_api(request):
    if request.method == 'GET':
        snippets = AUserbankDetails.objects.all()
        serializer = AUserbankDetailsSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AUserbankDetailsSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def companydetails_api(request):
    if request.method == 'GET':
        snippets = AUserworkDetails.objects.all()
        serializer = AUserworkDetailsSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AUserworkDetailsSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def motor_api(request):
    if request.method == 'GET':
        snippets = AMotorInsurance.objects.all()
        serializer = AMotorInsuranceSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AMotorInsuranceSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def author_api(request):
    if request.method == 'GET':
        snippets = Author.objects.all()
        serializer = AuthorSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    print(queryset)
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer'''

def odd(request):
    pass



class GeneralTipsViewSet(viewsets.ModelViewSet):
    queryset = Tips.objects.filter(insurance_type="general")
    serializer_class = TipsSerializer


class AutoTipsViewSet(viewsets.ModelViewSet):
    queryset = Tips.objects.filter(insurance_type="auto")
    serializer_class = TipsSerializer

class LifeTipsViewSet(viewsets.ModelViewSet):
    queryset = Tips.objects.filter(insurance_type="life")
    serializer_class = TipsSerializer

class HealthTipsViewSet(viewsets.ModelViewSet):
    queryset = Tips.objects.filter(insurance_type="health")
    serializer_class = TipsSerializer

