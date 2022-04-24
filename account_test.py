import unittest # Importing the unittest module
from account import Account # Importing the account class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("Twitter","KMalomba","passwaad") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_type,"Twitter")
        self.assertEqual(self.new_account.user_name,"KMalomba")
        self.assertEqual(self.new_account.password,"passwaad")


if __name__ == '__main__':
    unittest.main()
