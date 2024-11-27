
# PromptGround SDK

A simple Python SDK for interacting with the PromptGround API.

## Installation

Install the SDK using pip:

```bash
pip install promptground
```

## Usage

### Running a Prompt

To run a prompt and get the result, use the `run` method:

```python
from promptground.PromptGround import PromptGround

# Initialize the PromptGround object
pg = PromptGround(api_key="YOUR API KEY")

# Run a prompt
result = pg.run(
    alias='Typo-grammar fixer', 
    data={
        'text': 'this text explaining promptground but is not grammatically correct'
    }
)
print(result.content)  # Outputs the corrected text
print(result.usage)    # Outputs the usage details
```

### Understanding the Response Object

The `run` method returns a `PromptRunResult` object with the following attributes:

- `content` (str): The actual output of the prompt.
- `usage` (dict): The usage details which include:
  - `completion_tokens` (int): The number of tokens in the output.
  - `prompt_tokens` (int): The number of tokens in the input.
  - `total_tokens` (int): The total number of tokens (input + output).

Example:

```python
# Example response handling
print("Content:", result.content)  # The corrected text
print("Usage:", result.usage)      # The usage details
```

### Fetching Messages

If you want to fetch only the messages and run the prompt on your side, you can use the `messages` method:

```python
# Fetch messages
messages = pg.messages(
    alias='Typo-grammar fixer',
    data={
        'text': 'this text explaining promptground but is not grammatically correct'
    }
)
print(messages)  # Outputs a list of messages
```

## Methods

### `messages(alias, data={}, version=None)`

Fetch messages from the PromptGround API.

**Parameters:**
- `alias` (str): The prompt alias as seen on your dashboard.
- `data` (dict, optional): A flat object with key=value pairs used to substitute variables in the messages.
- `version` (str, optional): The specific prompt version ID to call. If not provided, the most recent prompt version will be used.

**Returns:**
- `list`: A list of messages. Each message is a dictionary with `content` and `role`. For example, `[{content: "message content", role: "system"}]`. The `role` can be `system`, `user`, or `assistant`.

### `run(alias, data={}, metadata={}, labels=[], model=None, version=None, response_format=None)`

Run a prompt and return the result.

**Parameters:**
- `alias` (str): The prompt alias as seen on your dashboard.
- `data` (dict, optional): A flat object with key=value pairs used to substitute variables in the messages.
- `metadata` (dict, optional): Additional data to help you filter in the "Runs" dashboard. It should be a flat key-value object.
- `labels` (list, optional): An array for distinguishing different prompts and filtering them afterward in the "Runs" dashboard.
- `model` (str, optional): The model to use for the prompt. If not provided, the most recent model will be used.
- `version` (str, optional): The specific prompt version ID to call. If not provided, the most recent prompt version will be used.
- `response_format` (str, optional): The response format for the prompt (e.g. `json_object`).

**Returns:**
- `PromptRunResult`: The result of running the prompt.

## Handling Results

The result of the `run` method is a `PromptRunResult` object with the following attributes:
- `content` (str): The actual output.
- `usage` (dict): The token usage details, which include:
  - `completion_tokens` (int): The number of tokens in the output.
  - `prompt_tokens` (int): The number of tokens in the input.
  - `total_tokens` (int): The total number of tokens (input + output).

## Exception Handling

Both `messages` and `run` methods will raise an `Exception` if there is an error with the API request. Be sure to handle these exceptions appropriately in your application.

## Contributions

If something is missing or you have any suggestions, please create an issue or open a pull request. For any questions or support, feel free to contact us.