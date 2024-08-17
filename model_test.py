import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)
models = client.models.list()
print(models)
print(models.data[0].id)

## chat model
messages = [
    {"role": "system", "content": "You are a standup comedian."},
    {"role": "user", "content": "Make me laugh like Tom and Jerry"},
  ]

response = client.chat.completions.create(
  model=models.data[0].id,
  messages=messages,
#   stream=True
)

reply = response.choices[0].message.content
print(reply)
print("-"*40)


messages.append(
    {"role": "assistant", "content": reply}
)

print(messages)