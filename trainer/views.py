from django.shortcuts import render
# Create your views here.
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login,logout
from PM import DB_Action, json_Action
from templates import registration
from django.contrib import messages
import re
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def trainer(request):
    print("")


def trainee(request):
    print("")

def admin(request):
    return render(request,"../templates/admin.html")



def adminAfterUpdate(request):
    id = request.POST.get('ID')
    userName = request.POST.get('userName')
    pwd = request.POST.get('password')
    Email = request.POST.get('Email')
    fullName = request.POST.get('fullName')
    role = request.POST.get('role')
    fullNameSplited = fullName.split(' ')
    firstName = fullNameSplited[0]
    lasttName = fullNameSplited[1]
    DB_Action.updateUser(id,firstName,lasttName,pwd,userName,Email,role)
    allusers = DB_Action.getAllUsers()
    facilities = json_Action.Sports_facilities()
    context = {"object_List": allusers, "facilities": facilities.distros_dict}
    return render(request, "admin2.html", context)

def showHomePage(request):
    return render(request, "../templates/homepage.html")

def showLogin(request):
    return render(request,"../templates/registration/sign-in.html")

def logout(request):
    auth.logout(request)
    messages.info(request,"You are now logout!")
    return redirect('/')

def afterFacilityUpdate(request,origName,origType,origOwner,origNeighborhood,origOperator,origOpenHours):
    name = request.POST.get('name')
    type = request.POST.get("type")
    neighborhood = request.POST.get("neighborhood")
    Operator = request.POST.get("Operator")
    Owner = request.POST.get("Owner")
    OpenHours = request.POST.get("OpenHours")
    facilityToUpdate={"Type":type,"Name":name,"Operator":Operator,"Owner":Owner,"neighborho":neighborhood,"OpenHours":OpenHours}
    originalFacility={"Type":origType,"Name":origName,"Operator":origOperator,"Owner":origOwner,"neighborho":origNeighborhood}
    facilities = json_Action.Sports_facilities()
    facilities.updateFacility(originalFacility,facilityToUpdate)
    allusers = DB_Action.getAllUsers()
    facilities = json_Action.Sports_facilities()
    context = {"object_List": allusers, "facilities": facilities.distros_dict}
    return render(request, "admin2.html", context)

def showRegister(request):
    return render(request, "../templates/registration/sign-up.html")

"""sign button clicked action, gets username and password from sign in page, and navigate to the right page"""
def loginBtn(request):
    uname = request.POST.get('username',False)
    pwd = request.POST.get('password',False)
    user = DB_Action.get_user_by_userName(uname)
    user["Email"] = user["E-mail"]
    if(user!= None and uname != None and pwd != None):
        if(user['password']==pwd):
            if (user['role'] == '1'):
                allusers = DB_Action.getAllUsers()
                facilities = json_Action.Sports_facilities()
                user["Email"] = user["E-mail"]
                context = {"user":user,"object_List" : allusers,"facilities" : facilities.distros_dict}
                return render(request, "admin2.html",context)
            if(user['role'] == '2'):
                neighborhoddList = json_Action.dict_neighborho.keys()
                facilitiesList = json_Action.dict_Type.keys()
                user["Email"] = user["E-mail"]
                context = {"user":user,"neighborhoddList":neighborhoddList,"facilities":facilitiesList,"id" : user['_id'],"username" : uname,"role": "2"}
                return render(request, "../templates/folder_trainer/trainer_web.html",context)
            if (user['role'] == '3'):
                neighborhoddList = json_Action.dict_neighborho.keys()
                facilitiesList = json_Action.dict_Type.keys()
                user["Email"] = user["E-mail"]
                context = {"user":user,"neighborhoddList":neighborhoddList,"facilities":facilitiesList,"id" : user['_id'],"username" : uname,"role": "3"}
                return render(request, "../templates/folder_trainee/web_trainee.html",context)
    return render(request,"registration/sign-in.html")

def delete_user(request,userID):
    DB_Action.removeUserByID(userID)
    allusers = DB_Action.getAllUsers()
    facilities = json_Action.Sports_facilities()
    context = {"object_List": allusers, "facilities": facilities.distros_dict}
    return render(request,"../templates/admin2.html",context)

def showUpdateUser(request, UserID):
    context = DB_Action.get_user_by_ID(UserID)
    context['firstName']="{} {}".format(context['firstName'],context['lastName'])
    context['id'] = context['_id']
    context['Email'] = context['E-mail']
    return render(request,"../templates/registration/update.html",{"user":context})

def addNewFacilities(request):
    if request.method == "POST":
        facilityType = request.POST.get("Field Type")
        print("dg,la;dgadgkad'lkgafdkh===================  ",facilityType)
        facilityName = request.POST.get('Field Name')
        facilityStreet = request.POST.get('Field Street')
        facilityHouseNumbe = request.POST.get('Field HouseNumbe')
        facilityNeighborho = request.POST.get('Field Neighborho')
        facilityOperator = request.POST.get('Field Operator')
        facilitySeats = request.POST.get('Field Seats')
        facilityActivity = request.POST.get('Field Activity')
        facilityFencing = request.POST.get('Field Fencing')
        facilityLighting = request.POST.get('Field Lighting')
        facilityHandicappe = request.POST.get('Field Handicappe')
        facilityCondition = request.POST.get('Field Condition')
        facilityOwner = request.POST.get('Field Owner')
        facilityForSchool = request.POST.get('Field ForSchool')
        facilityAssociatio = request.POST.get('Field Associatio')
        facilitySportType = request.POST.get('Field SportType')
        facilitylat = request.POST.get('Field lat')
        facilitylon = request.POST.get('Field lon')
        NewFacili = {
            'Type': facilityType,
            'Name': facilityName,
            'street': facilityStreet,
            'HouseNumbe': facilityHouseNumbe,
            'neighborho': facilityNeighborho,
            'Operator': facilityOperator,
            'Seats': facilitySeats,
            'Activity': facilityActivity,
            'fencing': facilityFencing,
            'lighting': facilityLighting,
            'handicappe': facilityHandicappe,
            'condition': facilityCondition,
            'Owner': facilityOwner,
            'ForSchool': facilityForSchool,
            'associatio': facilityAssociatio,
            'SportType': facilitySportType,
            'lat': facilitylat,
            'lon': facilitylon
        }
        json_Action.Add_New_Facility(NewFacili)
    return render(request, "admin2.html")



def deleteFacility(request, facilityId):
    jsonAct = json_Action.Sports_facilities()
    # faciltyToDelete = {"Type": facilityType,"Name":facilityName , "neighborho":facilityNeighborhood,"Operator": facilityOperator, "Owner": facilityOwner}
    jsonAct.delete_facility(facilityId)
    allusers = DB_Action.getAllUsers()
    facilities = json_Action.Sports_facilities()
    context = {"object_List": allusers, "facilities": facilities.distros_dict}
    return render(request, "admin2.html", context)


def backtoAdmin(request):
    allusers = DB_Action.getAllUsers()
    facilities = json_Action.Sports_facilities()
    context = {"object_List": allusers, "facilities": facilities.distros_dict}
    return render(request, "admin2.html", context)

def showUpdateFacility(request, facilityId):
       # facilityToUpdate = {"Type": facilityType,"Name":facilityName , "neighborho":facilityNeighborhood,"Operator": facilityOperator, "Owner": facilityOwner}
       users = DB_Action.getAllUsers()
       tmp = json_Action.Sports_facilities()
       tmp=tmp.distros_dict
       s = {}
       for obf in tmp:
           if(obf["id"]==facilityId):
               s= obf
               break
       if("OpenHours" not in s.keys()):
            s["OpenHours"] = " "
       context = {"myFacility":s,"users":users}
       return render(request,"updateFacility/updateFacility.html",context)


def ShowCourts(request):
    username=request.POST.get("userName")
    firstName=request.POST.get("firstName")
    lastName=request.POST.get("lastName")
    password=request.POST.get("password")
    Email=request.POST.get("Email")
    id=request.POST.get("id")
    role=request.POST.get("role")
    user={"userName":username,"firstName":firstName,"lastName":lastName,"password":password,"Email":Email,"role":role}
    role=user["role"]
    neighborhoddList = json_Action.dict_neighborho.keys()
    facilitiesList = json_Action.dict_Type.keys()
    selectedNeighbohood = request.POST.get("neighborhoods",False)
    facilityType = request.POST.get("facilitiesType",False)
    light = request.POST.get("lighting",False)
    jsonObj = json_Action.Sports_facilities()
    courts = []
    try:
        courts = jsonObj.get_by_type_neighborho(selectedNeighbohood, facilityType)
        if(light == "on"):
            courts = json_Action.modular_filtering(courts, "lighting", "כן")
        msg = True
    except KeyError as e:
        msg = False
    context = {"courtsList":courts,"neighborhoddList":neighborhoddList,"facilities":facilitiesList,"massege":msg,"id" : id,"username" : username,"role": role,"user" : user}
    if (role == "2"):

        return render(request,"../templates/folder_trainer/trainer_web.html",context)


    return render(request,"../templates/folder_trainee/web_trainee.html",context)


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



