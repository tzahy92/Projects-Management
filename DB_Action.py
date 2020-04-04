
from django.contrib import admin
from django.urls import path
import pymongo
from pymongo import MongoClient

urlpatterns = [
    path('admin/', admin.site.urls),
]

collection: MongoClient.address
cluster = MongoClient("mongodb+srv://yahelfr:29913051@cluster0-4iuqq.mongodb.net/test?retryWrites=true&w=majority")  ## connect to cluster
db = cluster["shareball"]  ##connect to database
collection = db["users"]  ##connect to collection
star = {"_id": 20 , "name": "yahel", "score": 10}
collection.insert_one(star)

