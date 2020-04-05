from django.contrib import admin
from django.urls import path
import pymongo
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://yahelfr:29913051@cluster0-4iuqq.mongodb.net/test?retryWrites=true&w=majority")  ## connect to cluster
db = cluster["shareball"]  ##connect to database
usersCollection = db["users"]  ##connect to collection


def insert_user(_id, userName, password, firstName, lastName, role):
    newUser = {"_id": _id, "userName": userName, "password": password, "firstName": firstName, "lastName": lastName,
               "role": role}
    usersCollection.insert_one((newUser))


def get_user_by_ID(_ID):
    return usersCollection.find_one({"_id": 20, "name": "yahel"})


def update_user_by_ID(_ID):
    usersCollection.update_one({"_id": 20}, {"$set": {"score": "30"}})
