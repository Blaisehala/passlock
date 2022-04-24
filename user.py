

class User:
  '''
  This class represents/generates the new instance of user
  '''

  def __init__(self,username,password):
    '''
    The __init__ method helps to define properties for our objects.The __init__ function is called every time an object is created from a class. 
    '''

    self.username = username
    self.password = password

  user_list = []

  
  def save_user(self):
    '''
    Save_user method saves the user object into the user list.
    '''
    User.user_list.append(self)

  def delete_user(self):
    '''
    delete_user method deletes the user object from the user list.
    '''
    User.user_list.remove(self)



class Accountcredentials:
  def __init__(self,account,username, password):
    self.account = account
    self.username = username
    self.password = password

  accountcredentials_list = []
  def save_accountcredentials(self):
    '''Saves the account credentials in the account credentials list.'''
    Accountcredentials.accountcredentials_list.append(self)