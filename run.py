#!/usr/bin/python3.8


from user import User,Credentials



def make_user(username, password):
    """ Function create_user takes in two arguments and creates a new user"""
    new_user = User(username, password) #Here we create a new object  new_user and return it
    return new_user


def s_user(user):
    ''' Function to save user'''
    user.save_user() #The Function takes in the user object and then calls the save_user  method to save the user.


def del_user(user):
    ''' Function to delete user'''
    user.delete_user()



def make_credentials(account,username,password):
    ''' Function to create new account credentials'''
    new_credentials = Credentials(account,username,password)
    return new_credentials


def s_credentials(user_credentials):
    ''' Function to save user  credentials'''
    user_credentials.save_credentials()



def del_credentials(user_credentials):
    ''' Function to  delete user credentials'''
    user_credentials.delete_credentials()
     
def login(name,password):
    return Credentials.verify_user(name,password)


def main():
  print('Hola! Welcome to WatchWord.')
    
  while True:
      '''
      cu-create-user
      lg-login
      ex-exit
      (shortcodes to be used while navigating the  app)  
      '''
      print("Use the following Shortcodes for your navigation🧭:\ncu -Create User\nlg -login\nex-exit")
      shortcodes = input().lower().strip()
      if shortcodes == "cu":
          print("Enter user details")
          print("-------------------")
          username = input('USERNAME\n')

          while True:
              print("Enter tp - to type your password\n gp - to generate password")
              password_choice = input('Choice').lower().strip()

              if password_choice == 'tp':
                  password = input('Password\n')
                  break
              elif password_choice == 'gp':
                  password = Credentials.generatePassword
                  break
              else:
                  print("Invalid password***.Use the shorcodes to generate password ")

          newuser = make_user(username, password)
        
      elif shortcodes== 'li':
            print ('Enter details to login')
            username= input('username')
            password= input('password')

          



            

        







if __name__=='__main__':
  main()



# print('Blaise')















