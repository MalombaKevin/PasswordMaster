from account import Account

def create_account(account_type,user_name,password):
    '''
    Function to create a new account
    '''
    new_account = Account(account_type,user_name,password)
    return new_account