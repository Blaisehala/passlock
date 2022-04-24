import unittest #importing unittest module
from user import User  #importing user2
from user import Credentials #importing credentials

class TestUser(unittest.TestCase):
  '''
  Test class for testing cases for the user class behavior
  '''

  def setUp(self): #Set up the method to run each test cases
   self.new_user = User("Blaise", "!@#$%^&*")

   #Teardown method
  def tearDown(self):
   User.user_list

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
    self.assertEqual(len(User.user_list),2) #CHECK CHECK ON THIS LINE AND THE ERROR TYPE


#Third test Case
  def test_delete_user(self):
    '''test_delete_user test method tests if the user object will be deleted'''
    self.new_user.save_user()
    test_user = User('Blaise','!@#$%^&*')
    test_user.save_user()

    self.new_user.delete_user()
    self.assertEqual(len(User.user_list),1) #CHECK CHECK


#Setting test Case for testing the class credentials

class TestCredentials(unittest.TestCase):
  '''Test credentials for testing cases for the credentials class behaviour'''

  def setUp(self):#Set up  the method to run each test case
    self.new_credentials=Credentials("twitter",'Blaise','!@#$%^&*')

#Fourth test Case
  def test_init(self):
    '''method tests for proper initialization'''
    self.assertEqual(self.new_credentials.account,'twitter')
    self.assertEqual(self.new_credentials.username,'Blaise')
    self.assertEqual(self.new_credentials.password,'!@#$%^&*')

#Fifth test case
  def test_save_credentials(self):
    ''' tests if the Save credentials method works properly'''
    self.new_credentials.save_credentials()#saving the new credentials 
    self.assertEqual(len(Credentials.credentials_list),3)

  
#sixth Test
  def test_delete_credentials(self):
    '''Test delete credentials to delete class credentials'''
    self.new_credentials.save_credentials()
    test_credentials = Credentials('account', 'username','password')
    test_credentials.save_credentials()
  
#seventh test
  def test_display_all_credentials(self):
    '''Method that returns a list of credentials'''
    self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)








if __name__ == '__main__':
    unittest.main()


