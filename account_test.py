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
    
    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account details
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(Account.account_details),1)
    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_details = []

# other test cases here
    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if I can save multiple account
            objects to my account_details
            '''
            self.new_account.save_account()
            test_account = Account("Test","user","testPassword") # new contact
            test_account.save_account()
            self.assertEqual(len(Account.account_details),2)


if __name__ ==  '__main__':
    unittest.main()



if __name__ == '__main__':
    unittest.main()
