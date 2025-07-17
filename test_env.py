from dotenv import load_dotenv
import os

load_dotenv()
print("API Key cargada:", os.getenv("OPENAI_API_KEY"))