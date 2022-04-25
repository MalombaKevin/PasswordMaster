from account import Account

def create_account(account_type,user_name,password):
    '''
    Function to create a new account
    '''
    new_account = Account(account_type,user_name,password)
    return new_account

def save_account(account):
    '''
    Function to save account
    '''
    account.save_account()

def del_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()

def find_account(account_type):
    '''
    Function that finds a account by account_type and returns the account
    '''
    return Account.find_by_account_type(account_type)


def check_existing_account(account_type):
    '''
    Function that check if a account exists with the account_type and return a Boolean
    '''
    return Account.account_exist(account_type)
