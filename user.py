from random import randint


class User:
    '''
    This class represents/generates the new instance of user
    '''

    def __init__(self, username, password):
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


class Credentials:
    def __init__(self, account, username, password):
        self.account = account
        self.username = username
        self.password = password

    credentials_list = []

    def save_credentials(self):
        '''Saves the  credentials in the  credentials list.'''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls,account):
        return cls.credentials_list

    @classmethod
    def search_credentials(cls, account):
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def verify_user(cls, username, password):
        active_user = ""
        for user in User.user_list:
            if (user.username == username and user.password == password):
                active_user = user, username

        return active_user

    def generatePassword(ln):
        characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'
        password = ''
        for i in range(ln):
            password += characters[randint(0, len(characters) - 1)]
        return password
