import os
import openai
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display


from openai import OpenAI

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)

if not client.api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
else:
    print("API key found and looks good so far!")

headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

#print(user_prompt_for(input_website))

messages = [
    {"role": "system", "content": "You are a Funny assistant"},
    {"role": "user", "content": "Tell me Ollama LLM joke"},
]

#To give you a preview -- calling OpenAI with system and user messages:

response = client.chat.completions.create(model="llama3.2", messages=messages)
print(response.choices[0].message.content)
