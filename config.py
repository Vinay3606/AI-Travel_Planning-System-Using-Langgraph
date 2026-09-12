import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


TAVILY_API_KEY=os.getenv('TAVILY_API_KEY')


AVIATION_STACK_API_KEY = os.getenv("AVIATION_STACK_API")

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

DATABASE_URL = os.getenv('DATABASE_URL')


def get_llm():
    return ChatOllama(model=os.getenv('OLLAMA_MODEL','llama3.2:3b'))