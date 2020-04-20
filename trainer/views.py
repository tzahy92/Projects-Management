from django.shortcuts import render
# Create your views here.
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from PM import DB_Action
from templates import registration
from django.contrib import messages
import re
from PM import json_Action
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def trainer(request):
    print("")


def trainee(request):
    print("")

def admin(request):
    return render(request,"../templates/admin.html")

def showHomePage(request):
    return render(request, "../templates/homepage.html")

def showLogin(request):
    return render(request,"../templates/registration/sign-in.html")

def showRegister(request):
    return render(request, "../templates/registration/sign-up.html")

"""sign button clicked action, gets username and password from sign in page, and navigate to the right page"""
def loginBtn(request):
    uname = request.POST.get('username',False)
    pwd = request.POST.get('password',False)
    user = DB_Action.get_user_by_userName(uname)
    if(user!= None and uname != None and pwd != None):
        if(user['password']==pwd):
            if (user['role'] == '1'):
                allusers = DB_Action.getAllUsers()
                context = {"object_List" : allusers}
                return render(request, "admin.html",context)
            if(user['role'] == '2'):
                return render(request, "../templates/folder_trainer/trainer_web.html")
            if (user['role'] == '3'):
                neighborhoddList = json_Action.lst_neighborho.keys()
                facilitiesList = json_Action.getFaciliies()
                context = {"neighborhoddList":neighborhoddList}
                return render(request, "../templates/folder_trainee/web_trainee.html",context)
    return render(request,"sign-in.html")

def delete_user(request,userID):
    DB_Action.removeUserByID(userID)
    return render(request,"../templates/admin.html")

def showUpdateUser(request, UserID):
    context = DB_Action.get_user_by_ID(UserID)
    context['firstName']="{} {}".format(context['firstName'],context['lastName'])
    context['id'] = context['_id']
    context['Email'] = context['E-mail']
    return render(request,"../templates/registration/update.html",{"user":context})


def register(request):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    uname = request.POST.get('usernameSignUp',False)
    firstpwd = request.POST.get('firstPasswordSignUp',False)
    secpwd = request.POST.get('secondPasswordSignUp',False)
    fullName = request.POST.get('fullName',False)
    email = request.POST.get('emailAdressSignUp',False)
    views = request.POST.get('fullName',False)
    if(firstpwd != secpwd):
        messages.info(request,'please enter same password')
        return render(request,"../templates/registration/sign-up.html")
    elif(DB_Action.checkUserNameExistence(uname)):
        messages.info(request, 'user name already Exist')
        return render(request, "../templates/registration/sign-up.html")
    elif(DB_Action.checkEmailExistence(email)):
        messages.info(request, 'email address already exist')
        return render(request, "../templates/registration/sign-up.html")
    elif(not re.search(regex,email)):
        messages.info(request, 'ilegal email address')
        return render(request, "../templates/registration/sign-up.html")
    elif (" " not in fullName):
        messages.info(request, 'ilegal name')
        return render(request, "../templates/registration/sign-up.html")
    else:
        DB_Action.insert_user(uname,firstpwd,fullName.split(" ")[0],fullName.split(" ")[1],'1',email)
        return render(request, "../templates/registration/sign-in.html")



