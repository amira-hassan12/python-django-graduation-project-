from dataclasses import field
import imp
import json
from msilib.schema import Class
from pyexpat import model
from.models import Gps, Image, Patient,Login,Signup_doctor,Signup_patient,Gps,Image,Ask,Answer, Review,Center
from.models import Doctor
from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields='__all__'
        
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields= '__all__'
        
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields= '__all__'
        
class Signup_doctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup_doctor
        fields= '__all__'
        
class Signup_patientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup_patient
        fields= '__all__'
        
                
class GpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gps
        fields= '__all__'
        
        


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields= '__all__'


class AskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ask
        fields= '__all__'
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields= '__all__'
class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model =Center
        fields= '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields= '__all__'