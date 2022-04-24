

class User:
  '''
  This class represents/generates the new instance of user
  '''
  user_list = []

  def __init__(self,usernamme,password):
    '''
    The __init__ method helps to define properties for our objects.The __init__ function is called every time an object is created from a class. 
    '''
    
    self.usernamme = usernamme
    self.password = password
  
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
