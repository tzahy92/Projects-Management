import unittest

# Create your tests here.
from PM import DB_Action


class MyTestCase(unittest.TestCase):


    def test_insert_to_DB(self):
        with self.assertRaisesRegex(Exception,"this ID is taken"):
            DB_Action.insert_user("23", "tzahy", "1234", "lab", "ja", 1)

if __name__ == '__main__':
    unittest.main()
