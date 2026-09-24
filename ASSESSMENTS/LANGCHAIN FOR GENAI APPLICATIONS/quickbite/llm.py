"""Shared optional LangChain model factory and offline-friendly response helpers."""
import os
from dotenv import load_dotenv
load_dotenv()

def configured_chat_model(temperature=0.3):
    provider=os.getenv("LLM_PROVIDER", "openai").lower()
    if provider == "ollama":
        from langchain_ollama import ChatOllama
        return ChatOllama(model=os.getenv("OLLAMA_MODEL", "llama3.1"), base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"), temperature=temperature)
    if os.getenv("OPENAI_API_KEY"):
        from langchain_openai import ChatOpenAI
        kwargs={"model":os.getenv("OPENAI_MODEL", "gpt-4o-mini"), "temperature":temperature}
        if os.getenv("BASE_URL"):
            kwargs["base_url"]=os.environ["BASE_URL"]
        return ChatOpenAI(**kwargs)
    return None

def demo_reply(text, history=""):
    """Small transparent fallback for running and demonstrating without credentials."""
    q=text.lower()
    if "how long" in q or "delivery" in q and "minute" in q:
        return "I can estimate delivery time once you share the route distance, item count, and weather."
    if "recommend" in q or "menu" in q or "food" in q or "cuisine" in q:
        return "I can suggest a dish from the menu. Tell me a cuisine or dietary preference and I’ll narrow it down."
    if "address" in q or "where" in q:
        return "I’ll use the delivery address you entered in the sidebar for this session."
    return "Thanks for your message! I’m QuickBite’s demo assistant. Add an LLM endpoint for natural, model-generated conversation."
