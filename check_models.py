from dotenv import load_dotenv
import os
from groq import Groq

# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# List models
models = client.models.list()
print("Models available for your key:")
for m in models:
    print("-", m)  # Just print the tuple or value directly