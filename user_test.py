import unittest #importing unittest module
from user import User  #importing user

class TestUser(unittest.TestCase):
  '''Test class for testing cases for the user class behavior
  '''

  def setUp(self): #Set up the method to run each test cases
   self.new_user = User("Blaise", "!@#$%^&*")

#First test Case 
  def test_init(self):

   '''test_init test method tests if the object is initialized properly
   '''
   self.assertEqual(self.new_user.username,"Blaise")
   self.assertEqual(self.new_user.password,"!@#$%^&*")

#Second test Case
  def test_save_user(self):
    '''test_save_user test method tests if the  object will be saved properly'''
    self.new_user.save_user() #saving the new contact
    self.assertEqual(self.new_user.username) #CHECK CHECK ON THIS LINE AND THE ERROR TYPE


#Third test Case
  def test_delete_user(self):
    '''test_delete_user test method tests if the user object will be deleted'''
    self.new_user.save_user()
    test_user = User('Blaise','!@#$%^&*')
    test_user.save_user()

    self.new_user.delete_user()
    self.assertEqual(self.new_user) #CHECK CHECK


if __name__ == '__main__':
    unittest.main()


