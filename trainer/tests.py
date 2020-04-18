#!/usr/bin/env python

import unittest
from django.test import TestCase

# Create your tests here.
from PM import DB_Action


class MyTestCase(unittest.TestCase):

    def test_insert_to_DB(self):
        with self.assertRaisesRegex(Exception,"this username is taken"): ##username already in the DB
            DB_Action.insert_user("user0", "1234","tzahy","maymon", 1,"tza@gmail.com")


    def test_get_user_ID(self):
        self.assertEqual(DB_Action.get_user_by_ID("001"),None)
        self.assertEqual(DB_Action.get_user_by_ID("23"),{"_id":"23","userName":"king","password":"2323","firstName":"lebron","lastName":"james","role":1})

    def test_get_user_by_userName(self):
        self.assertEqual(DB_Action.get_user_by_userName("tz"),None)
        self.assertEqual(DB_Action.get_user_by_userName("king"),{"_id":"23","userName":"king","password":"2323","firstName":"lebron","lastName":"james","role":1})

    def test_update_user_by_ID(self):
        with self.assertRaisesRegex(Exception, "this username is taken"):
            DB_Action.update_user_by_ID("23","userName","king")
        with self.assertRaisesRegex(Exception, "this ID is taken"):
            DB_Action.update_user_by_ID("001","id","23")

if __name__ == '__main__':
    unittest.main()
