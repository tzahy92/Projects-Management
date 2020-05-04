#!/usr/bin/env python

import unittest
from django.test import TestCase

# Create your tests here.
from PM import DB_Action


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

if __name__ == '__main__':
    unittest.main()
