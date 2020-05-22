from info.models import (
    Profile
)
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404

from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
User = get_user_model()
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
# Create your views here.
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from info.api.v0.serializers import(
ProfileSerializer,
ProfileReadSerializer
)

class profile(APIView):
    permission_classes = [AllowAny]
    #authentication_classes = (TokenAuthentication,)
    def post(self, request, *args, **kwargs):
        context={}
        data={}
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            Gender=serializer.validated_data['Gender']
            Height=serializer.validated_data['Height']
            Weight=serializer.validated_data['Weight']
            Activity=serializer.validated_data['Activity']
            Goals=serializer.validated_data['Goals']
            Height=Height/100
            Height=Height*Height
            BMI=Weight/Height
            x=1
            Age=serializer.validated_data['Age']
            a=serializer.validated_data['Height']
            if BMI <18.5:
                x=1
            elif BMI > 18.5 and BMI <25.0:
                x=2
            elif BMI>25.0 and BMI<30.0:
                x=3
            elif BMI >30.0:
                x=4
            BMR=1
            if Gender == '1' :
                BMR= (10*Weight)+(6.25*a)-(5*Age)+5       
            elif Gender == '2':
                print(BMR)
                BMR=   (10*Weight)+(6.25*a)-(5*Age)-161
            DailyCal=BMR
            if Activity=='1':
                DailyCal=BMR*1.2
            elif Activity =='2':
                DailyCal=BMR*1.4
            elif Activity =='3':
                DailyCal =BMR*1.6
            elif Activity =='4':
                DailyCal =BMR*1.75
            if Goals=='1':
                DailyCal=DailyCal- 1000
            elif Goals =='2':
                DailyCal=DailyCal- 500
            elif Goals =='3':
                DailyCal =DailyCal
            elif Goals =='4':
                DailyCal =DailyCal+ 500
            elif Goals =='5':
                DailyCal =DailyCal+ 1000
            user=get_object_or_404(User,id=3)
            serializer.save(User=user,BMI=BMI,Condition=x,BMR=BMR,DailyCalories=DailyCal)
            context['sucess']=True
            context['status']=200
            data=serializer.data
            data['BMI']=BMI
            data['Condition']=x
            context['data']=data
            return Response(context)
        else:
            context['sucess']=False
            context['status']=400
            data=serializer.errors
            context['data']=data
            return Response(context)

    def get(self, request, *args, **kwargs):
        context={}
        data={}
        try:
            us=get_object_or_404(User,id=3)
            obj=get_object_or_404(Profile,User=us)
        except:
            context['sucess']=False
            context['status']=400
            context['data']=data
            return Response(context)
        serializer = ProfileReadSerializer(obj)
        context['sucess']=True
        context['status']=200
        data=serializer.data
        context['data']=data
        return Response(context)

    def put(self, request, *args, **kwargs):
        us=get_object_or_404(User,id=3)
        obj=get_object_or_404(Profile,User=us)
        serializer = ProfileSerializer(obj,data=request.data)
        context={}
        data={}
        if serializer.is_valid():
            Gender=serializer.validated_data['Gender']
            Height=serializer.validated_data['Height']
            Weight=serializer.validated_data['Weight']
            Activity=serializer.validated_data['Activity']
            Goals=serializer.validated_data['Goals']
            Height=Height/100
            Height=Height*Height
            BMI=Weight/Height
            x=1
            Age=serializer.validated_data['Age']
            a=serializer.validated_data['Height']
            if BMI <18.5:
                x=1
            elif BMI > 18.5 and BMI <25.0:
                x=2
            elif BMI>25.0 and BMI<30.0:
                x=3
            elif BMI >30.0:
                x=4
            BMR=1
            if Gender == '1' :
                BMR= (10*Weight)+(6.25*a)-(5*Age)+5
            elif Gender == '2':
                BMR=   (10*Weight)+(6.25*a)-(5*Age)-161
            DailyCal=BMR
            if Activity=='1':
                DailyCal=BMR*1.2
            elif Activity =='2':
                DailyCal=BMR*1.4
            elif Activity =='3':
                DailyCal =BMR*1.6
            elif Activity =='4':
                DailyCal =BMR*1.75
            if Goals=='1':
                DailyCal=DailyCal- 1000
            elif Goals =='2':
                DailyCal=DailyCal- 500
            elif Goals =='3':
                DailyCal =DailyCal
            elif Goals =='4':
                DailyCal =DailyCal+ 500
            elif Goals =='5':
                DailyCal =DailyCal+ 1000
            serializer.save(User=us,BMI=BMI,Condition=x,BMR=BMR,DailyCalories=DailyCal)
            context['sucess']=True
            context['status']=200
            data=serializer.data
            data['BMI']=BMI
            data['Condition']=x
            context['data']=data
            return Response(context)
        context['sucess']=False
        context['status']=400
        data=serializer.errors
        context['data']=data
        return Response(context)
            
      