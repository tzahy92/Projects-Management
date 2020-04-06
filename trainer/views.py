from django.shortcuts import render
# Create your views here.
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from PM import DB_Action
def trainer(request):
    print("")


def trainee(request):
    print("")

def admin(request):
    print("")


"""sign button clicked action, gets username and password from sign in page, and navigate to the right page"""
def loginBtn(request):
    uname = request.POST.get('username',False)
    pwd = request.POST.get('password',False)
    user = DB_Action.get_user_by_userName(uname)
    if(user!= None and uname != None and pwd != None):
        if(user['password']==pwd):
            if (user['role'] == 1):
                return render(request, "admin.html")
            if(user['role'] == 2):
                return render(request, "../templates/folder_trainer/trainer_web.html")
            if (user['role'] == 3):
                return render(request, "../templates/folder_trainee/web_trainee.html")
    return render(request,"login.html")