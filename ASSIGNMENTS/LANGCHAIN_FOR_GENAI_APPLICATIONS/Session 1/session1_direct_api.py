"""Session 1: call the Chat Completions API directly and describe trade-offs."""
import os, requests
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Set OPENAI_API_KEY in .env to run this API call.")
else:
    try:
        response=requests.post(os.getenv("BASE_URL","https://api.openai.com/v1")+"/chat/completions",
          headers={"Authorization":f"Bearer {api_key}","Content-Type":"application/json"},
          json={"model":os.getenv("OPENAI_MODEL","gpt-3.5-turbo"),"messages":[{"role":"user","content":"Give one interesting fact about pani puri."}]},timeout=30)
        response.raise_for_status()
        print(response.json()["choices"][0]["message"]["content"])
    except requests.Timeout: print("Request timed out; retry with backoff or use an asynchronous job.")
    except requests.HTTPError as e: print("API returned an error:",e.response.status_code,e.response.text[:500])
    except requests.RequestException as e: print("Network error:",e)
print("Direct-call trade-offs: manual prompt/error/retry code; provider-specific response parsing; more work to compose retrieval, memory, and tools.")
