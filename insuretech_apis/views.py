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
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import re
apikey='''yourkey'''
#client = SendGridAPIClient(apikey)
client=''
def send_mail(email,subject,body,client=client):
    message = Mail(
        from_email='techinsure@bincom.com',
        to_emails=email,
        subject=subject,
        html_content=body)
    client.send(message)
def get_user(request):
    try:
        token = request.data.copy().get('token') if not request.POST else request.POST.copy().get('token')
        insurance_user = AInsuranceUserProfile.objects.get(token=token)
        return insurance_user
    except AInsuranceUserProfile.DoesNotExist:
        return None

def user_check(**kwargs):
    try:
        if kwargs.get('email'):
            email = kwargs['request'].data.copy().get('email') if not kwargs['request'].POST else kwargs['request'].POST.copy().get('email')
            insurance_user = AInsuranceUserProfile.objects.get(email=email)
        else:
            username = kwargs['request'].data.copy().get('password') if not kwargs['request'].POST else kwargs[
            'request'].POST.copy().get('password')
            insurance_user = AInsuranceUserProfile.objects.get(username=username)
        return  insurance_user
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
            return Response(serializer.data, )
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
        email = request.data.copy().get('email') if not request.POST else request.POST.copy().get('email')
        emailpattern = r'(^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
        password = request.data.copy().get('password') if not request.POST else request.POST.copy().get('password')
        passwordpattern = r'(?=[^0-9]*[0-9])(?=[a-zA-Z0-9\s]*[^a-zA-Z0-9\s])(?=(?:[^A-Z]*[A-Z]){1})\w{8,100}'
        subject = 'INSURE Tech'
        message = 'Welcome to insure '
        #send_mail(email,subject,message)
        serializer = AInsuranceUserProfileSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid() and (re.match(passwordpattern,password)if password else False) and (re.match(emailpattern,email) if email else False):
            if user_check(**{'request':request,'email':email}):
                content = {'status': 'failure', 'data': 'That email already exists'}
                return Response(content)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif not (re.match(emailpattern,email) if email else False):
            content = {'status': 'failure', 'data': 'wrong email format'}
            return Response(content)
        elif not (re.match(passwordpattern,password)if password else False):
            content = {'status': 'failure', 'data': 'wrong password format,make sure it contains 1 uppercase,a symbol and a number'}
            return Response(content)
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
            model_data = {'insuranceuserprofile': insurance_user.pk}
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
            model_data = {'insuranceuserprofile': insurance_user.pk}
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
            model_data = {'insuranceuserprofile': insurance_user.pk}
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
