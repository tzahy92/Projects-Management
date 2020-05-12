#!/usr/bin/env python

import unittest
from django.test import TestCase

# Create your tests here.
from PM import DB_Action
from PM import json_Action
import json
import os.path



              #   {"_id": "389", "userName": "admin89", "password": "1234", "firstName": "bar", "lastName": "butler",
                  #"role": "1","E-mail":"admin89@gmail.com"}


class MyTestCase(unittest.TestCase):

    def test_insert_to_DB(self):
        with self.assertRaisesRegex(Exception,"this username is taken"): ##username already in the DB
            DB_Action.insert_user("user0", "1234","admin89","maymon", "1","tza@gmail.com")


    def test_get_user_ID(self):
        self.assertEqual(DB_Action.get_user_by_ID("001"),None)
        self.assertEqual(DB_Action.get_user_by_ID("389"),{"_id": "389", "userName": "admin89", "password": "1234", "firstName": "bar", "lastName": "butler",
                  "role": "1","E-mail":"admin89@gmail.com"})

    def test_get_user_by_userName(self):
        self.assertEqual(DB_Action.get_user_by_userName("tz"),None)
        self.assertEqual(DB_Action.get_user_by_userName("admin89"),{"_id": "389", "userName": "admin89", "password": "1234", "firstName": "bar", "lastName": "butler",
                  "role": "1","E-mail":"admin89@gmail.com"})

    def test_update_user_by_ID(self):
        with self.assertRaisesRegex(Exception, "this username is taken"):
            DB_Action.update_user_by_ID("389","userName","admin89")
        with self.assertRaisesRegex(Exception, "this ID is taken"):
            DB_Action.update_user_by_ID("001","id","389")

    def test_get_all_sport_facility(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../PM/Sport.json")
        with open(path, encoding="utf8") as f:
            distros_dict = json.load(f)
        facility = json_Action.Sports_facilities()
        self.assertEqual(facility.get_distros_dict(),distros_dict)

    def test_get_filtered_sport_facility_(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../PM/Sport.json")
        with open(path, encoding="utf8") as f:
            distros_dict = json.load(f)
        facility = json_Action.Sports_facilities()
        #self.assertEqual(facility.get_by_type_neighborho('ג','קט-רגל'),[{'Type': 'קט רגל וינגייט', 'Name': '', 'street': 'וינגייט', 'HouseNumbe': '0.0', 'neighborho': 'ג', 'Operator': 'כיוונים', 'Seats': '0.0', 'Activity': '', 'fencing': '', 'lighting': 'כן', 'handicappe': '', 'condition': 'טוב מאוד', 'Owner': '', 'ForSchool': '', 'associatio': 'לא', 'SportType': '', 'lat': '31.256328799000073', 'lon': '34.802853764000076'}])
if __name__ == '__main__':
    unittest.main()
