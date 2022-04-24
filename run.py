#!/usr/bin/env python3.8

from user import User,Credentials



def make_user(username, password):
    """ Function create_user takes in two arguments and creates a new user"""
    new_user = User(username, password) #Here we create a new object  new_user and return it
    return new_user


def s_user(user):
    ''' Function to save user'''
    user.save_user() #The Function takes in the user object and then calls the save_user  method to save the user.



    


     
