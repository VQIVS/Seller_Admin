import requests
import datetime

"""" UserManager class Error handling"""

class UserManagerError(Exception):
    pass


"""" A class to handle the User management """
class UserManager:
    def __init__(self):
        self.base_url = 'https://topnet.justadmins.xyz/api/'
        self.headers = {"Content-Type": "application/json"}

    def get_token(self):
        url = self.base_url + 'admin/token'
        data = {
            "grant_type": "password",
            "username": "TopNet",
            "password": "Qi@s1383.83",
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            token = response.json()["access_token"]
            self.headers["Authorization"] = f"Bearer {token}"
        else:
            error_message = f'Error getting access token : {response.status_code}\nresponse body: {response.text}'
            raise UserManagerError(error_message)
