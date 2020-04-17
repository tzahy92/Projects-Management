from django.shortcuts import render
# Create your views here.
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from PM import DB_Action
from templates import registration
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def trainer(request):
    print("")


def trainee(request):
    print("")

def admin(request):
    print("")

def showLogin(request):
    return render(request,"../templates/registration/sign-in.html")

"""sign button clicked action, gets username and password from sign in page, and navigate to the right page"""
def loginBtn(request):
    uname = request.POST.get('username',False)
    pwd = request.POST.get('password',False)
    user = DB_Action.get_user_by_userName(uname)
    if(user!= None and uname != None and pwd != None):
        if(user['password']==pwd):
            if (user['role'] == '1'):
                return render(request, "admin.html")
            if(user['role'] == '2'):
                return render(request, "../templates/folder_trainer/trainer_web.html")
            if (user['role'] == '3'):
                return render(request, "../templates/folder_trainee/web_trainee.html")
    return render(request,"sign-in.html")
    ##return render(request, "../templates/folder_trainer/trainer_web.html")

def register(request):
    uname = request.POST.get('usernameSignUp',False)
    firstpwd = request.POST.get('firstPasswordSignUp',False)
    secpwd = request.POST.get('secondPasswordSignUp',False)
    email = request.POST.get('emailAdressSignUp',False)
    views = request.POST.get('fullName',False)
    if(firstpwd != secpwd):
        messages.info(request,'please enter same password')
        return render(request,"../templates/registration/sign-up.html")
    elif(DB_Action.checkUserNameExistence(uname)):
        messages.info(request, 'userNamealreadyExist')
        return render(request, "../templates/registration/sign-up.html")
    elif(DB_Action.checkEmailExistence(email)):
        messages.info(request, 'email adress already exist')
        return render(request, "../templates/registration/sign-up.html")
    else:
        return render(request, "../templates/folder_trainer/trainer_web.html")



