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

    def creat(self, num, data_limit):
        url = self.base_url + 'user'
        now = datetime.datetime.now()
        expire = now + datetime.timedelta(days=30)
        expire_seconds = int(expire.timestamp())
        data = {
            "username": f"TN_{num}",
            "proxies": {
                "vmess": {},
                "vless": {}
            },
            "inbounds": {
                "vmess": [
                    "VMess TCP",
                    "VMess Websocket"
                ],
                "vless": [
                    "VLESS TCP REALITY 8443",
                    "VLESS TCP REALITY 2056"
                ]
            },
            "expire": expire_seconds,
            "data_limit": data_limit,
            "data_limit_reset_strategy": "no_reset",
            "status": "active",
            "note": "This user is for TopNet VPN provider.",
        }
        response = requests.post(url, json=data, headers=self.headers)
        if response.status_code != 200:
            error_message = f'Error creating user: {response.status_code}\nresponse body: {response.text}'
            raise UserManagerError(error_message)

