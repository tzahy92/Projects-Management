import copy

from django.contrib import admin
from django.urls import path
from pymongo import MongoClient

"""this file connecting all the other files to the project's data base"""

cluster = MongoClient("mongodb+srv://yahelfr:29913051@cluster0-4iuqq.mongodb.net/test?retryWrites=true&w=majority")  ## connect to cluster
db = cluster["shareball"]  ##connect to database
usersCollection = db["users"]  ##connect to collection


""" get user details and insert a new user to database"""
def insert_user(userName,password,firstName,lastName,role,Email):
    if(get_user_by_userName(userName)!=None):
        raise Exception("this username is taken")
    ##if(get_user_by_ID(_id)!=None):
     ##   raise Exception("this ID is taken")
    else:
        newUser = {"userName" : userName,"password" : password, "firstName": firstName,"lastName":lastName, "role": role,"E-mail":Email}
        usersCollection.insert_one((newUser))


""""get user ID and returns all user details"""
def get_user_by_ID(_ID):
    return usersCollection.find_one({"_id":_ID})

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
    #return userlist
