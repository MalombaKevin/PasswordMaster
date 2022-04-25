import random
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
    print("Greetings Earthling. Welcome to PasswordMaster. Enter your name:")
    
    passwordMaster_user_name = input()

    print(f"Hi {passwordMaster_user_name}.PasswordMaster at your service. How can I help you?")
    # print("\U00001F601")
    print('\n')
    while True:
                    print("Use the following shortcodes  ca - create a new account | all - display  all accounts | fa -find an account | x -delete account | q -quit PasswordMaster ")

                    short_code = input().lower()

                    if short_code == 'ca':


                            print ("Enter Account type: [ eg Twitter/ Facebook/ Paypal / GMAIL / etc]") #account input
                            account_type = input()

                            print("Enter Account user name  ")   #Username input
                            user_name = input()

                            print ("Enter your password")
                            password = input()

                        #     print("Enter Account Password : Choose A for Bot generated Password or B to input password ")
                        #     choice = input()
                        #     if choice == "A or a":
                        #            password = print(random.randit(300000000, 10000000000000))
                        #     elif choice == "B or b":
                        #             password =input()
                            
                        # #     password = input()

            
                            save_account(create_account(account_type,user_name,password)) 
                            print ('\n')
                            print('***' * 20)
                            print(f"New [{account_type}] account with a username [{user_name}] and password [{password}] created")
                            print ('\n')


                        #     print(" Select : ca - create a new account | all - display  all accounts | fa -find an account | x -delete account | q -quit PasswordMaster ")
                
                    elif short_code == 'fa':

                        #     print("Enter the account you want to search for")

                            search_account_type= input()
                            if check_existing_account(search_account_type):
                                    search_account = find_account(search_account_type)
                                    print(f"Your Search results:")
                                    print('*' * 20)
                                    print(f"Account Type............{search_account_type}")
                                    print(f"Account User Name.......{search_account.user_name}")
                                    print(f"Account Password........{search_account.password}")
                            else:
                                    print("Sorry. PasswordMaster could not find your account!. Select ca to create an account")
                   
                #     elif short_code == "x":

                #             print("Enter the account you want to search for")
                #             if del_account():
                            
                                    

                    elif short_code == 'all':

                            if display_account():
                                    print("Here is a list of all your accounts, their usernames and passwords")
                                    print('\n')

                                    for account in display_account():
                                            
                                            print(f"Account Type: {account.account_type}  {account.account_type} User Name: {account.user_name}  Password: {account.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any accounts saved yet. Select ca to save an account")
                                    print('\n')

                    elif short_code == "q":
                            print("Thank you for using PasswordMaster. Your security is our concern. Ciao!")
                            break
                    else:
                            print("Sorry PasswordMaster didn't understand your codes. Try again using the codes given")

                 

   
if __name__ == '__main__':

    main()
