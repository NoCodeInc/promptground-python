import requests
from .models.PromptRunResult import PromptRunResult
from .utils.validation import (
    ensure_is_string,
    ensure_object_is_flat
)

class PromptGround:
    """
    A class to interact with the PromptGround API.

    Attributes:
    api_key (str): The API key for authentication.
    base_url (str): The base URL for the API.
    context (dict): Context information about the SDK.
    """

    def __init__(self, api_key, base_url="https://api.promptground.io/v2"):
        """
        Initialize the PromptGround object.

        Args:
        api_key (str): The API key for authentication.
        base_url (str): The base URL for the API.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.context = {
            'sdk': 'python',
            'sdk-version': '1.1.1'
        }

    def messages(self, alias, data={}, version=None) -> list:
        """
        Fetch messages from the API.

        Args:
        alias (str): The alias for the prompt.
        data (dict): The data for the prompt.
        version (str, optional): The version of the prompt.

        Returns:
        list: A list of messages.

        Raises:
        Exception: If there is an error fetching messages.
        """
        ensure_is_string(alias, name='alias')
        
        url = f"{self.base_url}/prompt/messages"
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
            return response.json().get('data', {}).get('messages', [])
        else:
            raise Exception(response.json().get("message", "Error fetching messages"))
        
    def run(self, alias, data={}, metadata={}, labels=[], model=None, version=None, response_format=None) -> PromptRunResult:
        """
        Run a prompt and return the result.

        Args:
        alias (str): The alias for the prompt.
        data (dict): The data for the prompt.
        metadata (dict, optional): Metadata for the prompt.
        labels (list, optional): Labels for the prompt.
        model (str, optional): The model to use for the prompt.
        version (str, optional): The version of the prompt.
        response_format (str, optional): The response format for the prompt.

        Returns:
        PromptRunResult: The result of running the prompt.

        Raises:
        Exception: If there is an error running the prompt.
        """
        ensure_is_string(alias, name='alias')
        ensure_object_is_flat(data, name='data')
        ensure_object_is_flat(metadata, name='metadata')
        ensure_object_is_flat(labels, name='labels')
    
        url = f"{self.base_url}/prompt/run"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "alias": alias,
            "data": data,
            "metadata": metadata,
            "labels": labels,
            "context": self.context
        }
        
        if version:
            payload['version'] = version

        if model:
            payload['model'] = model

        if response_format:
            payload['response_format'] = response_format

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200 and response.json().get("success", False):
            result = response.json().get('data', {})
            return PromptRunResult(
                result.get('result', ''),
                result.get('usage', {})
            )
        else:
            raise Exception(response.json().get("message", "Error running prompt"))
