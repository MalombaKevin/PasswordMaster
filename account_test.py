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

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_details = []


    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if I can save multiple account
            objects to my account_details
            '''
            self.new_account.save_account()
            test_account = Account("Tibapedia","user","passwaad") # new contact
            test_account.save_account()
            self.assertEqual(len(Account.account_details),2)
    
    def test_delete_account(self):
            '''
            test_delete_account to test if I can remove an account from my account details
            '''
            self.new_account.save_account()
            test_account = Account("Tibapedia","user", "passwaad") # new contact
            test_account.save_account()

            self.new_account.delete_account()# Deleting a contact object
            self.assertEqual(len(Account.account_details),1)
   
    def test_find_account_by_account_type(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_account.save_account()
        test_account = Account("Tibapedia","user","passwaad") 
        test_account.save_account()

        found_account = Account.find_by_account_type("TIbapedia")

        # self.assertEqual()
 

if __name__ ==  '__main__':
    unittest.main()



if __name__ == '__main__':
    unittest.main()
