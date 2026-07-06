import requests
from dotenv import load_dotenv
import json

load_dotenv()

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer Api_key",
  },
  data=json.dumps({
    "model": "poolside/laguna-xs-2.1",
    "max_tokens":1000,
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ]
  })
)

response_json = response.json()

data = response.json()

print(data["choices"][0]["message"]["content"])


# Usage
usage = response_json.get("usage", {})

print("\nUsage:")
print(f"Prompt Tokens     : {usage.get('prompt_tokens', 0)}")
print(f"Completion Tokens : {usage.get('completion_tokens', 0)}")
print(f"Reasoning Tokens  : {usage.get('completion_tokens_details', {}).get('reasoning_tokens', 0)}")
print(f"Total Tokens      : {usage.get('total_tokens', 0)}")
print(f"Cost              : ${usage.get('cost', 0):.8f}")