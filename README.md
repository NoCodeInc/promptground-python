# PromptGround SDK

A simple Python SDK for interacting with the PromptGround API.

## Installation

Install the SDK using pip:

```bash
pip install promptground
```

## Usage

```python
from promptground import PromptGround

pg = PromptGround(api_key="YOUR API KEY")
prompt = pg.prompt(alias='welcome-user', data={'name': 'PromptGround'})
print(prompt) # Outputs "Welcome to PromptGround"