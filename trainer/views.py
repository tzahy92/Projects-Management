from django.shortcuts import render

# Create your views here.
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from  django.contrib.auth.models import User, auth

def submit(request):
    print("i made it")
    f = open("C:\\Users\\admin\\Desktop\\demo.txt", "a")
    f.write("Now the file has more content!")
    f.close()
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not  None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,'login.html')