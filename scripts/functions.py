import requests
from scripts.model import UserManager, UserManagerError

user_obj = UserManager()

""" A function to create a new user """


def create_connection(data, start, end):
    for number in range(start, end):
        try:
            user_obj.creat(number, data)
            print("Success")
        except UserManagerError as e:
            print(f"Failed: {e}")


""" A function to get and save the user subscription link """
