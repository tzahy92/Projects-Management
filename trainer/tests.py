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
    def setUp(self) -> None:
        my_path = os.path.abspath(os.path.dirname(__file__))
        self.path = os.path.join(my_path, "../PM/temp.json")
        with open(self.path, encoding="utf8") as f:
            self.distros_dict = json.load(f)["Sports"]

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

        facility = json_Action.Sports_facilities()
        self.assertEqual(facility.get_distros_dict(),self.distros_dict)

    def test_get_filtered_sport_facility_(self):
        facility = json_Action.Sports_facilities()
        print(json_Action.modular_filtering(facility.get_by_type_neighborho('ג',"כל-המתקנים"),"lighting","כן"))
        self.assertEqual(facility.get_by_type_neighborho('ג','קט-רגל'),[{'Type': 'קט רגל וינגייט', 'Name': '', 'street': 'וינגייט', 'HouseNumbe': '0.0', 'neighborho': 'ג', 'Operator': 'כיוונים', 'Seats': '0.0', 'Activity': '', 'fencing': '', 'lighting': 'כן', 'handicappe': '', 'condition': 'טוב מאוד', 'Owner': '', 'ForSchool': '', 'associatio': 'לא', 'SportType': '', 'lat': '31.256328799000073', 'lon': '34.802853764000076', 'id': '142'}])

    def test_get_filtered_sport_facility_by_ligth(self):
        user_name = "admin89"
        if (DB_Action.checkUserNameExistence(user_name)==False):
            raise Exception("this user name {} not exist".format(user_name))

        user = DB_Action.get_user_by_userName(user_name)
        if(json_Action.check_permission(user)== False):
            raise Exception("this user {} do not have permission".format(user_name))

        facilities_result =[{'Type': "מגרש ספורט משולב – 43X32 מ'", 'Name': 'רמב"ם', 'street': 'קדושי בגדד', 'HouseNumbe': '1.0', 'neighborho': "ג'", 'Operator': 'ניהול עצמי', 'Seats': '0.0', 'Activity': 'פתוח ללא הגבלה', 'fencing': 'קיים גידור', 'lighting': 'קיימת תאורה', 'handicappe': 'נגיש לנכים', 'condition': 'תקין ופעיל', 'Owner': 'עיריית באר שבע', 'ForSchool': 'רמב"ם', 'associatio': '', 'SportType': '', 'lat': '31.252959540000063', 'lon': '34.77930799000006', 'id': '20'}, {'Type': "אצטדיון/מסלול אתלטיקה קלה – 6-4 מסלולים, 250 או 300 מ'", 'Name': "מקיף א'", 'street': 'דרך השלום', 'HouseNumbe': '15.0', 'neighborho': "ג'", 'Operator': 'כיוונים', 'Seats': '0.0', 'Activity': 'פתוח ללא הגבלה', 'fencing': 'קיים גידור', 'lighting': 'קיימת תאורה', 'handicappe': 'נגיש לנכים', 'condition': 'תקין ופעיל', 'Owner': 'עיריית באר שבע', 'ForSchool': "מקיף א'", 'associatio': '', 'SportType': '', 'lat': '31.252697283000032', 'lon': '34.801092856000025', 'id': '59'}, {'Type': "מגרש כדורגל – 45X90 מ'", 'Name': 'טאובל', 'street': 'בן גוריון', 'HouseNumbe': '0.0', 'neighborho': "ג'", 'Operator': 'כיוונים', 'Seats': '0.0', 'Activity': 'בתיאום בלבד', 'fencing': 'קיים גידור', 'lighting': 'קיימת תאורה', 'handicappe': 'נגיש לנכים', 'condition': 'תקין ופעיל', 'Owner': 'עיריית באר שבע', 'ForSchool': '', 'associatio': '', 'SportType': '', 'lat': '31.253835614000025', 'lon': '34.813499412000056', 'id': '66'}, {'Type': 'מגרש טניס', 'Name': 'טאובל', 'street': 'בן גוריון', 'HouseNumbe': '0.0', 'neighborho': "ג'", 'Operator': 'כיוונים', 'Seats': '0.0', 'Activity': 'פתוח ללא הגבלה', 'fencing': 'קיים גידור', 'lighting': 'קיימת תאורה', 'handicappe': 'נגיש לנכים', 'condition': 'תקין ופעיל', 'Owner': 'עיריית באר שבע', 'ForSchool': '', 'associatio': '', 'SportType': '', 'lat': '31.255589585000052', 'lon': '34.812797157000034', 'id': '67'}, {'Type': "מגרש כדורסל – 19X32 מ'", 'Name': 'נטעים', 'street': 'גולומב', 'HouseNumbe': '0.0', 'neighborho': "ג'", 'Operator': 'ניהול עצמי', 'Seats': '0.0', 'Activity': 'פתוח ללא הגבלה', 'fencing': 'קיים גידור', 'lighting': 'קיימת תאורה', 'handicappe': 'נגיש לנכים', 'condition': 'תקין ופעיל', 'Owner': 'עיריית באר שבע', 'ForSchool': 'נטעים', 'associatio': '', 'SportType': '', 'lat': '31.25481152900005', 'lon': '34.80434551500008', 'id': '77'}, {'Type': "אולם ספורט קטן – 20x10 מ'", 'Name': 'נטעים', 'street': 'גולומב', 'HouseNumbe': '0.0', 'neighborho': "ג'", 'Operator': 'ניהול עצמי', 'Seats': '0.0', 'Activity': 'בתיאום בלבד', 'fencing': 'קיים גידור', 'lighting': 'קיימת תאורה', 'handicappe': 'נגיש לנכים', 'condition': 'תקין ופעיל', 'Owner': 'עיריית באר שבע', 'ForSchool': 'נטעים', 'associatio': '', 'SportType': '', 'lat': '31.254599988000052', 'lon': '34.80413410500006', 'id': '78'}, {'Type': "מגרש כדורסל – 19X32 מ'", 'Name': 'אולפנת אמי"ת', 'street': 'וינגייט', 'HouseNumbe': '0.0', 'neighborho': "ג'", 'Operator': 'כיוונים', 'Seats': '0.0', 'Activity': 'פתוח ללא הגבלה', 'fencing': 'קיים גידור', 'lighting': 'קיימת תאורה', 'handicappe': 'נגיש לנכים', 'condition': 'תקין ופעיל', 'Owner': 'עיריית באר שבע', 'ForSchool': 'אמי"ת', 'associatio': '', 'SportType': '', 'lat': '31.254698034000057', 'lon': '34.801090842000065', 'id': '88'}, {'Type': "אולם ספורט בינוני – 32x19 מ'", 'Name': 'אולפנת אמי"ת', 'street': 'וינגייט', 'HouseNumbe': '0.0', 'neighborho': "ג'", 'Operator': 'כיוונים', 'Seats': '100.0', 'Activity': 'בתיאום בלבד', 'fencing': 'קיים גידור', 'lighting': 'קיימת תאורה', 'handicappe': 'נגיש לנכים', 'condition': 'תקין ופעיל', 'Owner': 'עיריית באר שבע', 'ForSchool': 'אמי"ת', 'associatio': 'מכבי דרום', 'SportType': 'התעמלות אומנותית', 'lat': '31.254729720000057', 'lon': '34.800717803000055', 'id': '89'}, {'Type': "אולם ספורט קטן – 20x10 מ'", 'Name': 'דגניה', 'street': "ז'בוטינסקי", 'HouseNumbe': '17.0', 'neighborho': "ג'", 'Operator': 'ניהול עצמי', 'Seats': '0.0', 'Activity': 'בתיאום בלבד', 'fencing': 'קיים גידור', 'lighting': 'קיימת תאורה', 'handicappe': 'נגיש לנכים', 'condition': 'תקין ופעיל', 'Owner': 'עיריית באר שבע', 'ForSchool': '', 'associatio': '', 'SportType': '', 'lat': '31.24996042300006', 'lon': '34.80812192500008', 'id': '98'}, {'Type': "אולם ספורט קטן – 15x24 מ'", 'Name': 'חזון עובדיה', 'street': 'גוש עציון', 'HouseNumbe': '13.0', 'neighborho': "ג'", 'Operator': 'ניהול עצמי', 'Seats': '0.0', 'Activity': 'בתיאום בלבד', 'fencing': 'קיים גידור', 'lighting': 'קיימת תאורה', 'handicappe': 'נגיש לנכים', 'condition': 'תקין ופעיל', 'Owner': 'עיריית באר שבע', 'ForSchool': '', 'associatio': '', 'SportType': '', 'lat': '31.253308584000024', 'lon': '34.80797698500004', 'id': '102'}, {'Type': "מגרש ספורט משולב – 43X32 מ'", 'Name': 'טאובל', 'street': 'בן גוריון', 'HouseNumbe': '0.0', 'neighborho': "ג'", 'Operator': 'כיוונים', 'Seats': '0.0', 'Activity': 'פתוח ללא הגבלה', 'fencing': 'קיים גידור', 'lighting': 'קיימת תאורה', 'handicappe': 'נגיש לנכים', 'condition': 'תקין ופעיל', 'Owner': 'עיריית באר שבע', 'ForSchool': '', 'associatio': '', 'SportType': '', 'lat': '31.255115363000073', 'lon': '34.813026809000064', 'id': '103'}, {'Type': "אולם ספורט בינוני – 32x19 מ'", 'Name': "מקיף א'", 'street': 'דרך השלום', 'HouseNumbe': '15.0', 'neighborho': "ג'", 'Operator': 'כיוונים', 'Seats': '0.0', 'Activity': 'בתיאום בלבד', 'fencing': 'קיים גידור', 'lighting': 'קיימת תאורה', 'handicappe': 'נגיש לנכים', 'condition': 'תקין ופעיל', 'Owner': 'עיריית באר שבע', 'ForSchool': "מקיף א'", 'associatio': 'ניקה,מכבי, כיוונים', 'SportType': 'ריקודים, כדורסל, נכים', 'lat': '31.252473181000028', 'lon': '34.80021493900006', 'id': '116'}, {'Type': "מגרש ספורט משולב – 43X32 מ'", 'Name': "מקיף א'", 'street': 'דרך השלום', 'HouseNumbe': '15.0', 'neighborho': "ג'", 'Operator': 'כיוונים', 'Seats': '0.0', 'Activity': 'פתוח ללא הגבלה', 'fencing': 'קיים גידור', 'lighting': 'קיימת תאורה', 'handicappe': 'נגיש לנכים', 'condition': 'תקין ופעיל', 'Owner': 'עיריית באר שבע', 'ForSchool': "מקיף א'", 'associatio': '', 'SportType': '', 'lat': '31.252804155000035', 'lon': '34.80168226600006', 'id': '120'}, {'Type': 'קט רגל וינגייט', 'Name': '', 'street': 'וינגייט', 'HouseNumbe': '0.0', 'neighborho': 'ג', 'Operator': 'כיוונים', 'Seats': '0.0', 'Activity': '', 'fencing': '', 'lighting': 'כן', 'handicappe': '', 'condition': 'טוב מאוד', 'Owner': '', 'ForSchool': '', 'associatio': 'לא', 'SportType': '', 'lat': '31.256328799000073', 'lon': '34.802853764000076', 'id': '142'}, {'Type': 'מתקן אימון כושר גופני', 'Name': 'פארק מרמלדה', 'street': "שד' בן גוריון", 'HouseNumbe': '0.0', 'neighborho': "שכונה ג'", 'Operator': 'כיוונים', 'Seats': '0.0', 'Activity': 'כן', 'fencing': 'כן', 'lighting': 'כן', 'handicappe': '', 'condition': '', 'Owner': '', 'ForSchool': '', 'associatio': '', 'SportType': '', 'lat': '31.259607209000023', 'lon': '34.81121359200006', 'id': '165'}]
        facility = json_Action.Sports_facilities()
        filtered_facilities = facility.get_by_type_neighborho('ג',"כל-המתקנים")
        self.assertEqual(json_Action.modular_filtering(filtered_facilities,"lighting","כן"),facilities_result)


if __name__ == '__main__':
    unittest.main()
