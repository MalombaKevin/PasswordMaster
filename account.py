class Account:
    """
    Class that generates new instances of accounts.
    """

    account_details = [] # Empty account details 

    def __init__(self,account_type,user_name,password):

      
        self.account_type = account_type
        self.user_name = user_name
        self.password = password
        