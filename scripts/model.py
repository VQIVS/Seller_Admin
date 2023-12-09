import requests
import datetime
import json

"""" UserManager class Error handling"""


class UserManagerError(Exception):
    pass


"""" A class to handle the User management """


class UserManager:
    def __init__(self, config_path='config.json'):
        with open(config_path) as config_file:
            config = json.load(config_file)

        self.base_url = config.get('base_url')
        self.headers = {"Content-Type": "application/json"}
        self.username = config.get('username')
        self.password = config.get('password')

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

    def create(self, num, data_limit):
        url = self.base_url + 'user'
        now = datetime.datetime.now()
        expire = now + datetime.timedelta(days=30)
        expire_seconds = int(expire.timestamp())
        data = {
            "username": f"USER{num}",
            "proxies": {
                "vmess": {},
                "vless": {}
            },
            "expire": expire_seconds,
            "data_limit": data_limit,
            "data_limit_reset_strategy": "no_reset",
            "status": "active",
        }
        response = requests.post(url, json=data, headers=self.headers)
        if response.status_code != 200:
            error_message = f'Error creating user: {response.status_code}\nresponse body: {response.text}'
            raise UserManagerError(error_message)

    def sublink(self, username):
        url = self.base_url + f'user/{username}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            user_data = response.json()
            if "subscription_url" in user_data:
                sub_link = user_data["subscription_url"]
                return sub_link
            else:
                raise UserManagerError("Subscription URL not found")
        elif response.status_code == 404:
            raise UserManagerError("User not found")
        else:
            error_message = f'Error: {response.status_code}'
            raise UserManagerError(error_message)

    def reset_usage(self):
        # not usable yet
        pass
