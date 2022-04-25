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
    Function that finds an account by account_type and returns the account
    '''
    return Account.find_by_account_type(account_type)


def check_existing_account(account_type):
    '''
    Function that check if an account exists with the account_type and return a Boolean
    '''
    return Account.account_exist(account_type)

def display_account():
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_account()


def main():
    print("Greetings Earthlings. Welcome to PasswordMaster. Enter your name:")
    passwordMaster_user_name = input()

    print(f"Hi {passwordMaster_user_name}.PasswordMaster at your service. How can I help you?")
    print('\n')
    while True:
                    print("Use these short codes : ca - create a new account, da - display account, fa -find an account, q -quit PasswordMaster")

                    short_code = input().lower()

                    if short_code == 'ca':


                            print ("Enter Account type: [ Twitter/ Facebook/ Paypal]") #account input
                            account_type = input()

                            print("Enter Account user name  ")   #Username input
                            user_name = input()

                            print("Enter Account Password")
                            password = input()

            
                            save_account(create_account(account_type,user_name,password)) 
                            print ('\n')
                            print(f"New Account for {account_type} with a username {user_name} created")
                            print ('\n')

                    elif short_code == "q":
                            print("Thank you for using PasswordMaster. Your security is our concern. Ciao!")
                            break
                    else:
                            print("Sorry PasswordMaster didn't understand your codes. Try again using the codes given")

                 

   
if __name__ == '__main__':

    main()
