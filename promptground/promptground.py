import requests

class PromptGround:
    def __init__(self, api_key, base_url = "https://api.promptground.io/v1"):
        self.api_key = api_key
        self.base_url = base_url

    def prompt(self, alias, version=None, data={}, default=None):
        url = f"{self.base_url}/prompt"

        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "alias": alias,
            "data": data
        }
        
        if version:
            payload['version'] = version

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200 and response.json().get("success", False):
            return response.json().get('data', {}).get('prompt', '')
        else:
            if default:
                return default
            raise Exception(response.json().get("message", "Error fetching prompt"))