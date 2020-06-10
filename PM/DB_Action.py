import copy

from django.contrib import admin
from django.urls import path
from pymongo import MongoClient

"""this file connecting all the other files to the project's data base"""

cluster = MongoClient("mongodb+srv://yahelfr:29913051@cluster0-4iuqq.mongodb.net/test?retryWrites=true&w=majority")  ## connect to cluster
db = cluster["shareball"]  ##connect to database
usersCollection = db["users"]  ##connect to collection
coachRatingCollection = db["coachRating"]
facilityRatingCollection = db["facilityRating"]

def insertCoachRate(rate,coach):
    print("********************************************************")
    print(rate)
    print("********************************************************")
    coachRate = coachRatingCollection.find_one({"coach_id":coach["_id"]})
    if (coachRate != None):
        ##y= coachRate["numOfrates"]
        coachRate["numOfrates"] += 1
        coachRate["AVGrate"] = (int(coachRate["AVGrate"]) + int(rate))/int(coachRate["numOfrates"])
        coachRatingCollection.update_one({"coach_id":coach["_id"]},{"$set":{"AVGrate":coachRate["AVGrate"]},"$inc":{"numOfrates":1}})
    else:     ##coach dosent have a rate yet
        mycoach = {"coach_id":coach["_id"],"coachFirstName":coach["firstName"],"coachLastName":coach["lastName"],"Email":coach["E-mail"],"numOfrates":1,"AVGrate":rate}
        coachRatingCollection.insert_one(mycoach)


def getAllCoachRates():
    coachRates = list(coachRatingCollection.find({}))
    return coachRates


""" get user details and insert a new user to database"""
def insert_user(userName,password,firstName,lastName,role,Email):
    if(get_user_by_userName(userName)!=None):
        raise Exception("this username is taken")
    ##if(get_user_by_ID(_id)!=None):
     ##   raise Exception("this ID is taken")
    else:
        newUser = {"userName" : userName,"password" : password, "firstName": firstName,"lastName":lastName, "role": role,"E-mail":Email}
        usersCollection.insert_one((newUser))
    return True

""""get user ID and returns all user details"""
def get_user_by_ID(_ID):
    return usersCollection.find_one({"_id":_ID})

def getcoachRate_by_id(_id):
    return coachRatingCollection.find_one({"coach_id":_id})


def removeUserByUserNamer(userName):
    usersCollection.remove({"userName":userName})

def removeUserByID(id):
    usersCollection.remove({"_id":id})

"""get user ID, field to update in DB and value to update, then makes the update in DB"""
def update_user_by_ID(_ID,field,value):
    if (field == "userName" and get_user_by_userName(value) != None):
        raise Exception("this username is taken")
    if (field == "id" and get_user_by_ID(value) != None):
        raise Exception("this ID is taken")
    usersCollection.update_one({"_id":_ID},{"$set":{field:value}})
"""get user-name and return all user's details from DB"""
def get_user_by_userName(username):
    return usersCollection.find_one({"userName": username})

def checkUserNameExistence(username):
    return  usersCollection.find_one({"userName": username}) != None

def checkEmailExistence(email):
    return  usersCollection.find_one({"E-mail": email}) != None

def updateUser(ID,firstName,lastName,password,userName,Email,role):
    print("$$$$$$$$$$$$$$$$$$$$$ {} {} {} {} {} {}".format(ID,firstName,lastName,password,userName,Email))
    newValues = {"firstName":firstName,"lastName":lastName,"password":password,"userName":userName,"E-mail":Email,"role":role}
    ##bulk.find({"_id":ID}).update({"$set":{"password":password}})
    usersCollection.update({"_id":ID},newValues)

def getAllUsers():
    userlist = list(usersCollection.find({}))
    newuser = {}
    newusersList = []
    for user in userlist:
        newuser['id'] = user['_id']
        newuser['userName'] = user['userName']
        newuser['password'] = user['password']
        newuser['firstName'] = user['firstName']
        newuser['lastName'] = user['lastName']
        newuser['role'] = user['role']
        newuser['Email'] = user['E-mail']
        usertoadd = copy.deepcopy(newuser)
        newusersList.append(usertoadd)
    return newusersList

