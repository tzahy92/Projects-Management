from django.contrib import admin
from django.urls import path
import pymongo
from pymongo import MongoClient

collection: MongoClient.address

cluster = MongoClient("mongodb+srv://yahelfr:29913051@cluster0-ufupc.mongodb.net/test?retryWrites=true&w=majority")  ## connect to cluster
db = cluster["tryout"]  ##connect to database
collection = db["students"]  ##connect to collection

star = {"_id": 50 , "name": "elhanan", "score": 15}
collection.insert_one(star)

