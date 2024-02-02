import requests
import hmac
import hashlib
from datetime import datetime

class PromptGround:
    def __init__(self, api_key, api_secret, base_url = "https://api.promptground.io/v1"):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        self.access_token = self.obtain_access_token()

    def create_signature(self, key, secret_key, timestamp):
        data = f"{key}#{secret_key}#{timestamp}"
        return hmac.new(secret_key.encode(), data.encode(), hashlib.sha256).hexdigest()

    def obtain_access_token(self):
        timestamp = int(datetime.utcnow().timestamp())
        signature = self.create_signature(self.api_key, self.api_secret, timestamp)
        url = f"{self.base_url}/token"
        payload = {
            "key": self.api_key,
            "signature": signature,
            "timestamp": timestamp
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200 and response.json().get("success", False):
            return response.json()['data']['token']
        else:
            error_message = response.json().get("message", "Error obtaining access token")
            raise Exception(error_message)

    def prompt(self, alias, data=None, default=None):
        if data is None:
            data = {}
        url = f"{self.base_url}/prompt"
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        payload = {
            "alias": alias,
            "data": data
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200 and response.json().get("success", False):
            return response.json()['data']['prompt']
        else:
            if default:
                return default
            raise Exception(response.json().get("message", "Error fetching prompt"))