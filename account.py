class Account:
    """
    Class that generates new instances of accounts.
    """

    account_details = [] # Empty account details 

    def __init__(self,account_type,user_name,password):

      
        self.account_type = account_type
        self.user_name = user_name
        self.password = password
    
    account_details = [] # Empty contact list
 # Init method up here
    def save_account(self):

        '''
        save_account method saves account objects into account_details
        '''

        Account.account_details.append(self)
    
    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_details
        '''

        Account.account_details.remove(self)
    
    @classmethod
    def find_by_account_type(cls,account_type):
        '''
        Method that takes in an account type and returns a username and password that matches account type searched.

        Args:
            account_type : Type of account
        Returns :
            username and password associated with account searched
        '''

        for account in cls.account_details:
            if account.account_type == account_type:
                return account