import email
from unicodedata import name
from django.db import models

# Create your models here.


class Patient(models.Model):
    f_name = models.CharField(max_length=190,null=False)
    l_name = models.CharField(max_length=190,null=False)
    password=models.CharField(max_length=190,null=True)
    conf_password=models.CharField(max_length=190,null=True)
    email =models.CharField(max_length=190,null=True)
    phone =models.CharField(max_length=190,null=True)
    age =models.CharField(max_length=190,null=True)
    address=models.CharField(max_length=190,null=True)
    
    def __str__(self):
        return self.f_name
    
    


class Doctor(models.Model):
    f_name = models.CharField(max_length=190,null=False)
    l_name = models.CharField(max_length=190,null=False)
    password=models.CharField(max_length=190,null=True)
    conf_password=models.CharField(max_length=190,null=True)
    address =models.CharField(max_length=190,null=True)
    email =models.CharField(max_length=190,null=True)
    phone =models.CharField(max_length=190,null=True)
    age =models.CharField(max_length=190,null=True)
    
    
    def __str__(self):
        return self.f_name    
    
class Login(models.Model):
    email = models.CharField(max_length=190,null=True)
    password= models.CharField(max_length=190,null=True)
    
    
    
    def __str__(self):
        return self.email  
    
    
class Signup_doctor(models.Model):
    f_name = models.CharField(max_length=190,null=False)
    l_name = models.CharField(max_length=190,null=False)
    password=models.CharField(max_length=190,null=True)
    conf_password=models.CharField(max_length=190,null=True)
    address =models.CharField(max_length=190,null=True)
    email =models.CharField(max_length=190,null=True)
    
    
            
        
    def __str__(self):
        return self.f_name  
        
        
        
class Signup_patient(models.Model):
    f_name = models.CharField(max_length=190,null=False)
    l_name = models.CharField(max_length=190,null=False)
    password=models.CharField(max_length=190,null=True)
    conf_password=models.CharField(max_length=190,null=True)
    email =models.CharField(max_length=190,null=True)
    age =models.CharField(max_length=190,null=True)
        
    def __str__(self):
        return self.f_name
    
    
    
class Gps(models.Model):
    location = models.CharField(max_length=190,null=True)
    
    
    def __str__(self):
        return self.location  
    
    
class Image(models.Model):
    pic = models.ImageField()
    
    
    def __str__(self):
        return self.pic 

class Ask(models.Model):
    patient=models.ForeignKey(Patient,related_name='ask',on_delete=models.CASCADE)
    question=models.CharField(max_length=190,null=False,)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.question 

class Answer(models.Model):
    doctor=models.ForeignKey(Doctor,related_name='answer',on_delete=models.CASCADE)
    question = models.ForeignKey(Ask,on_delete=models.CASCADE,null=True)
    answer=models.CharField(max_length=190,null=False, )
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str (self.question )

class Center(models.Model):
    doctor=models.ForeignKey(Doctor,models.CASCADE)
    center_name=models.CharField(max_length=190,null=False)
    address=models.CharField(max_length=190,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.center_name 

class recommendeddoctor(models.Model):
    doctor=models.ForeignKey(Doctor,models.CASCADE)
    doctor_name=models.CharField(max_length=190,null=False)
    address=models.CharField(max_length=190,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.center_name
    
class Review (models.Model):
    patient=models.ForeignKey(Patient,models.CASCADE)
    center_name=models.ForeignKey(Center,on_delete=models.CASCADE,null=True)
    rate=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str (self.rate)






