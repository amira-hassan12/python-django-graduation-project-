from ast import Return
from multiprocessing import context

from urllib import response
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import *
from.json import DoctorSerializer, PatientSerializer,Signup_patientSerializer,Signup_doctorSerializer,LoginSerializer,GpsSerializer,ImageSerializer,AskSerializer,AnswerSerializer,ReviewSerializer,CenterSerializer
from rest_framework.views import APIView,View

import json
import stripe
from django.conf import settings
from rest_framework import status
from django.shortcuts import redirect

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

#class patient_LIST(APIView):
   #  def get(self,request):
        # p1 =patient.object.all()
        # p2 =PatientSerializer(p1,many=True)
        # Return Response(p2.data)
          
class patient_LIST(viewsets.ModelViewSet): 
     queryset =Patient.objects.all()  
     serializer_class =PatientSerializer


class doctor_LIST(viewsets.ModelViewSet): 
     queryset =Doctor.objects.all()  
     serializer_class = DoctorSerializer


class login_LIST(viewsets.ModelViewSet): 
     queryset =Login.objects.all()  
     serializer_class = LoginSerializer
     
class signup_doctor_LIST(viewsets.ModelViewSet): 
     queryset =Signup_doctor.objects.all()  
     serializer_class = Signup_doctorSerializer
     
class signup_patient_LIST(viewsets.ModelViewSet): 
     queryset =Signup_patient.objects.all()  
     serializer_class = Signup_patientSerializer


class gps(viewsets.ModelViewSet): 
     queryset =Gps.objects.all()  
     serializer_class = GpsSerializer


class image(viewsets.ModelViewSet): 
     queryset =Image.objects.all()  
     serializer_class = ImageSerializer

class ask_LIST(viewsets.ModelViewSet): 
     queryset =Ask.objects.all()  
     serializer_class = AskSerializer

class answer_LIST(viewsets.ModelViewSet): 
     queryset =Answer.objects.all()  
     serializer_class = AnswerSerializer

class center_LIST(viewsets.ModelViewSet): 
     queryset =Center.objects.all()  
     serializer_class = CenterSerializer

class recommendeddoctor_LIST(viewsets.ModelViewSet): 
     queryset =Center.objects.all()  
     serializer_class = RecommendeddoctorSerializer

class review_LIST(viewsets.ModelViewSet): 
     queryset =Review.objects.all()  
     serializer_class = ReviewSerializer


class StripeCheckoutView(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': 'price_xxxx',
                        'quantity': 1,
                    },
                ],
                payment_method_types=['card',],
                mode='payment',
                success_url= + '/?',
                cancel_url= + '/?',
            )

            return redirect(checkout_session.url)
        except:
            return Response(
                {'error': 'Something went wrong when creating stripe checkout session'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )









