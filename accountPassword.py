class Accountpassword:
    """
    Class that generates new instances of passwords
    """
    account_details = []
    
    def _init_(self,account_type, user_name, password):
         """
       _ init_methdd that help describe the properties of my object
         Args:
         account_type : New account type
         user_name: New account username
         password: New account password
    
          """
         self.account_type = account_type
         self.user_name = user_name
         self.password = password

