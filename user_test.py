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
    self.new_user.save_user() #saving the new contact
    self.assertEqual(self.new_user.username)
  


if __name__ == '__main__':
    unittest.main()


