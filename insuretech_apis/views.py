from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import *
import json
from .serializers import *
from django.views.decorators.csrf import csrf_exempt

def get_user(request):
    try:
        token = request.data.copy().get('token') if not request.POST else request.POST.copy().get('token')
        insurance_user = AInsuranceUserProfile.objects.get(token=token)
        return insurance_user
    except AInsuranceUserProfile.DoesNotExist:
        return None

@csrf_exempt
@api_view(['POST',])
def profile_update_api(request):
    snippets = get_user(request)
    if request.method == 'POST':
        if snippets:
            serializer = AInsuranceUserProfileSerializer(snippets, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST',])
def profile_api(request):
    snippets = get_user(request)
    if request.method == 'POST':
        if snippets:
            serializer = AInsuranceUserProfileSerializer(snippets,)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST',])
def profile_login_api(request):
    #works
    try:
        email = request.data.copy().get('email') if not request.POST else request.POST.copy().get('email')
        snippets = AInsuranceUserProfile.objects.get(username=email)
    except AInsuranceUserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        serializer = AInsuranceUserProfileSerializer(snippets)
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

@csrf_exempt
@api_view(['POST',])
def bankdetails_create_api(request):
    insurance_user = get_user(request)
    if request.method == 'POST':
        if insurance_user:
            dummy = request.data
            del dummy['token']
            model_data = {'insuranceuserprofile', insurance_user}
            model_data.update(dummy)
            serializer = AUserbankDetailsSerializer(data=model_data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST',])
@renderer_classes([JSONRenderer])
def bankdetails_view_api(request,):
    insurance_user = get_user(request)
    if request.method == 'POST':
        if insurance_user:
            snippets = insurance_user.auserbankdetails_set.all()
            dj = [AUserbankDetailsSerializer(i).data for i in snippets]
            content = {'status': 'success', 'data': dj}
        else:
            content = {'status': 'not_found', 'data': {}}
        return Response(content)

@csrf_exempt
@api_view(['POST',])
def companydetails_create_api(request):
    insurance_user = get_user(request)
    if request.method == 'POST':
        if insurance_user:
            dummy = request.data
            del dummy['token']
            model_data = {'insuranceuserprofile', insurance_user}
            model_data.update(dummy)
            serializer = AUserworkDetailsSerializer(data=model_data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST',])
@renderer_classes([JSONRenderer])
def companydetails_view_api(request,):
    insurance_user = get_user(request)
    if request.method == 'POST':
        if insurance_user:
            snippets = insurance_user.auserworkdetails_set.all()
            dj = [AUserworkDetailsSerializer(i).data for i in snippets]
            content = {'status': 'success', 'data': dj}
        else:
            content = {'status': 'not_found', 'data': {}}
        return Response(content)


@csrf_exempt
@api_view(['POST',])
def auto_insurance_create_api(request):
    insurance_user = get_user(request)
    if request.method == 'POST':
        if insurance_user :
            dummy = request.data
            del dummy['token']
            model_data = {'insuranceuserprofile', insurance_user}
            model_data.update(dummy)
            serializer = AMotorInsuranceSerializer(data=model_data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST',])
@renderer_classes([JSONRenderer])
def auto_insurance_view_api(request,):
    insurance_user = get_user(request)
    if request.method == 'POST':
        if insurance_user:
            snippets = insurance_user.amotorinsurance_set.all()
            dj=[AMotorInsuranceSerializer(i).data for i in snippets]
            content = {'status':'success','data': dj}
            #serializer = AMotorInsuranceSerializer(snippets,many=True) works but not sweet
            #return Response(serializer.data,)
        else:
            content = {'status': 'not_found', 'data': {}}
        return Response(content)
        #return HttpResponse(json.dumps(dj),content_type='text/json') works

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
