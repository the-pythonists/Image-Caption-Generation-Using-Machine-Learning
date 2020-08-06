from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.views import LoginView    

from LoginApp.models import *

class SessionCheckView(View):
    def get(self,request):
        if request.session.has_key('user'):
            user = request.session['user']
            return JsonResponse({'Result':True})
        return JsonResponse({'Result':False})

class RegisterView(View):
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

    def get(self,request):
        return render(request,'registerAccount.html')

class LoginView(View):
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Register.objects.filter(Email=email):
            ecryptPass = Register.objects.get(Email=email).Password
            if check_password(password,ecryptPass):
                request.session['user'] = email
                # return HttpResponseRedirect('/home')
                return render(request,'album.html',{'user':request.session['user']})
            else:
                return render(request,'signin.html',{'msg':'Incorrect Email or Password'})
        else:
            return render(request,'signin.html',{'msg':'No Account Found'})

    def get(self, request):
        return render(request,'signin.html')

def logout(request):
    if request.session.has_key('user'):
        del request.session['user']
    return HttpResponseRedirect('/home')


class AdminLogin(LoginView):
    template_name = 'signin.html'


class HomeClass(View):
    def get(self, request):
        return HttpResponse('home')    