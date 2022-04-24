#!/usr/bin/env python3.8

from user import User,Credentials


""" Function create_user creates a new user"""
def create_user(username, password):
    new_user = User(username, password)
    return new_user



