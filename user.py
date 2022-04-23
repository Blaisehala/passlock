

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
