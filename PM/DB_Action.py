
from django.contrib import admin
from django.urls import path
import pymongo
from pymongo import MongoClient



cluster = MongoClient("mongodb+srv://yahelfr:29913051@cluster0-4iuqq.mongodb.net/test?retryWrites=true&w=majority")  ## connect to cluster
db = cluster["shareball"]  ##connect to database
usersCollection = db["users"]  ##connect to collection


def insert_user(_id,userName,password,firstName,lastName,role):
    if(get_user_by_userName(userName)!=None):
        raise Exception("this username is taken")
    if(get_user_by_ID(_id)!=None):
        raise Exception("this ID is taken")
    else:
        newUser = {"_id": _id,"userName" : userName,"password" : password, "firstName": firstName,"lastName":lastName, "role": role}
        usersCollection.insert_one((newUser))

def get_user_by_ID(_ID):
    return usersCollection.find_one({"_id":_ID})

def update_user_by_ID(_ID,field,value):
    if (field == "userName" and get_user_by_userName(value) != None):
        raise Exception("this username is taken")
    if (field == "id" and get_user_by_ID(field) != None):
        raise Exception("this ID is taken")
    usersCollection.update_one({"_id":20},{"$set":{field:value}})

def get_user_by_userName(username):
    return usersCollection.find_one({"userName": username})










