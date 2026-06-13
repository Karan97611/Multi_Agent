from dotenv import load_dotenv
from langchain_ollama import ChatOllama
import os
load_dotenv()


def get_llm():
    """
    Central place to create LLM.

    If later you want to switch
    from Ollama to OpenAI
    you only change code here.
    """

    return ChatOllama(
        model=os.getenv("MODEL_NAME"),
        temperature=0.3
    )