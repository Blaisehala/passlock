#!/usr/bin/python3.8
from user import User, Credentials



def make_user(username, password):
    """ Function create_user takes in two arguments and creates a new user"""
    new_user = User(username, password)  # Here we create a new object  new_user and return it
    return new_user


def s_user(user):
    ''' Function to save user'''
    User.save_user(user) # The Function takes in the user object and then calls the save_user  method to save the user.


def del_user(user):
    ''' Function to delete user'''
    User.delete_user(user)


def make_credentials(account, username, password):
    ''' Function to create new account credentials'''
    new_credentials = Credentials(account, username, password)
    return new_credentials


def s_credentials(user_credentials):
    ''' Function to save user  credentials'''
    return Credentials.save_credentials(user_credentials)

def display_credentials(account):
    return Credentials.display_credentials(account)

    
def del_credentials(user_credentials):
    ''' Function to  delete user credentials'''
    return user_credentials.delete_credentials()

def search_credentials(account):
    return Credentials.search_credentials(account)


def login(name, password):
    return Credentials.verify_user(name, password)


def generatePassword(ln):
    return Credentials.generatePassword(ln)


def main():
    print('HOLA! WELCOME TO WATCHWORD\n \\\\\\///\n.\t \\\\\\///--> -->\n \\\\\\///\n')

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
                    password = Credentials.generatePassword(12)
                    print(password)
                    break
                else:
                    print("Invalid password***.Use the shorcodes to generate password ")

            s_user(make_user(username, password))
            print(f"✅Created user{username} {password}")
            

            newuser = make_user(username, password)


        elif shortcodes=="ex":
            print('✘ exited')
            break

        


        elif shortcodes == 'lg':
            print('☎ Enter details to login')
            username = input('username')
            password = input('password')



            user = login(username, password)
            print(f' ⛩ welcome to Watchword {username}')

            # break
          

            

            while True:
                print('*' *60)
                print(
                        'Use the following shortcodes for your way around:\ncc -Create new credentials \ndc -Display credentials\nfc-Find credentials\ndel-Delete credentials\next -exit app\n')

                shortcodes == input("Enter Option:").lower().strip()
               
                if shortcodes == 'ext':
                    print('Bye Bye')
                    break

                elif shortcodes=='cc':
                     print('Save credentials.')
                     account = input('Enter account name:').strip()
                     username= input('Account username:').strip()
                     while True:
                         print('Enter tp- to type password\n gp- to generate new password')
                         password_choice = input('Choice:').strip()
                         if password_choice == 'tp':
                             password= input('password')

                             break
                        
                         elif password_choice == 'gp':
                             password= generatePassword(8)
                             break

                         else:
                             print('Invalid password***.Use the shorcodes to generate password')

                     make_credentials(s_credentials(account, username, password))

                     print(f'Your{account} has been created.\n Your Username is {username} and Password is {password}')

                elif shortcodes== 'fc':
                    print("Enter your account name")
                    user_credentials= input('Account Name').strip()
                    if s_credentials(user_credentials):
                        account=s_credentials(user_credentials)
                        print("Your account is now available")

                    else:
                        print("Account not found")

                elif shortcodes== 'dc':
                    if display_credentials(username):
                        print("Welcome")
                        for i in display_credentials(username):
                            print("{credential.account}\t {credential.username}\t {credential.password}")
                    else:
                        print("You dont have any credentials")    

                elif  shortcodes== 'del':
                    print("Enter Account Name")
                    search = (input('Enter Account Name')).strip()
                    if search_credentials(search):
                        account = search_credentials(search)
                        del_credentials(account)
                        print("Account successfully deleted")
                    else:
                        print("Account not found")
            else:

                print("Please Create a new account")

        else:
            print("Invalid.! Please try again")
                    





                        















if __name__ == '__main__':
    main()

# print('Blaise')
