from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.views.generic import View

from LoginApp.models import *

class LoginView(View):
    def post(self, request):
        fName = request.POST.get('fName')
        lName = request.POST.get('lName')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        gender = request.POST.get('gender')[0]
        email = request.POST.get('email')
        securityQuestion = request.POST.get('securityQuestion')
        securityAnswer = request.POST.get('securityAnswer')

        if Register.objects.filter(Email=email):
            messages.success(request,f"Account Already Present with {email} !!")
            return render(request,'registerAccount.html')
        else:
            Register(FirstName=fName,LastName=lName,Password=make_password(password),
            SecurityQuestion=securityQuestion,SecurityAnswer=securityAnswer,Gender=gender,Email=email).save()
            messages.success(request,f"Welcome Aboard: {fName} {lName} !!")
            return render(request,'registerAccount.html')


    def get(self, request):
        return render(request,'registerAccount.html')

def test(request):
    return HttpResponse('test fn')