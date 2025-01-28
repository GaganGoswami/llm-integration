import openai
from IPython.display import display, Markdown
from openai import OpenAI

openai = OpenAI(
    base_url = 'http://localhost:1234/v1',
    api_key='ollama', # required, but unused
)


# Function to stream OpenAI completion
def stream_openai_completion(prompt):
    response = openai.chat.completions.create(
        model="mistral-7b",  # or "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}]
    )
    print(response.choices[0].message.content)

# Example usage
prompt = "Explain the concept of quantum computing in simple terms."
stream_openai_completion(prompt)