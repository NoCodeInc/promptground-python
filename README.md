# PromptGround SDK

A simple Python SDK for interacting with the PromptGround API.

## Installation

Install the SDK using pip:

pip install promptground


## Usage

```python
from promptground import PromptGround

pg = PromptGround(api_key="your_api_key_id", api_secret="your_api_secret")
prompt = pg.prompt(alias='welcome-user', data={'name': 'PromptGround'})
print(prompt) # Outputs "Welcome to PromptGround"