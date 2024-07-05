# import os
# from dotenv import load_dotenv

# from langchain.llms import OpenAI
# from langchain.llms import HuggingFaceHub

# # Use the environment variables to retrieve API keys
# load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# HUGGINGFACEHUB_API_KEY = os.getenv("HUGGINGFACEHUB_API_KEY")

# # Initialize OpenAI LLM with the API key
# llm_openai = OpenAI(model_name="text-davinci-003", api_key=OPENAI_API_KEY)

# # Initialize Hugging Face LLM without the api_key parameter
# llm_huggingface = HuggingFaceHub(repo_id="google/flan-t5-large")

# our_query = "What is python ?"
# completion_openai = llm_openai(our_query)
# print(completion_openai)

# our_query = "Describe about mahendra singh dhoni?"
# completion_huggingface = llm_huggingface(our_query, api_key=HUGGINGFACEHUB_API_KEY)
# print(completion_huggingface)

#lets write a code using both openai and huggiface llms
# import os
# from dotenv import load_dotenv #what is this used for 

# from langchain_openai import OpenAI

# # Use the environment variables to retrieve API keys
# load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# # Initialize OpenAI LLM with the API key
# print(OPENAI_API_KEY)


# print("Initializing OpenAI LLM...")

# openai_client = OpenAI(api_key=OPENAI_API_KEY)
# # Example usage: Generate text using OpenAI LLM
# prompt = "Write a short story about AI."
# response = openai_client.generate(prompts=[prompt])
# print("OpenAI LLM Response:", response.generations[0].text)




import os
from dotenv import load_dotenv  # Used to load environment variables from a .env file
import httpx

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Check if the API key is loaded correctly
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key is not set properly in the environment variables.")

print("OpenAI API Key:", OPENAI_API_KEY)
print("Initializing OpenAI LLM...")

# Import the updated module
from langchain_openai import OpenAI

# Initialize OpenAI LLM with the API key
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Example usage: Generate text using OpenAI LLM
prompt = "Write a short story about AI."

# Use httpx with SSL verification disabled for OpenAI API call
try:
    with httpx.Client(verify=False) as client:
        openai_response = client.post(
            "https://api.openai.com/v1/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "text-davinci-003",
                "prompt": prompt,
                "max_tokens": 500
            }
        )
        if openai_response.status_code == 200:
            print("OpenAI LLM Response:", openai_response.json()['choices'][0]['text'])
        else:
            print("Error:", openai_response.text)
except httpx.ConnectError:
    print("SSL verification failed. Please check your SSL certificates.")
