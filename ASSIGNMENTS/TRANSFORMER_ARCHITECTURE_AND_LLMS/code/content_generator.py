"""Session 6 Tasks 3 & 5 - AI Content Generator.
Task 3 : generate_blog(topic)                  -> short blog post (max_tokens = 100)
Task 5 : generate_blog_v2(topic, tone, ...)    -> improved version (ONE suggestion implemented: an engaging
         prompt template - tone + catchy title + hook + call-to-action - and a bigger token budget).
Uses the OpenAI REST API through `requests` (the old openai.Completion.create() call from the hint was removed in
openai>=1.0 - this is its modern equivalent: /v1/chat/completions with max_tokens). Set OPENAI_API_KEY to use it;
without a key an offline template is returned so the code always runs."""
import os
import requests

API_URL = "https://api.openai.com/v1/chat/completions"


def _call_gpt(system, user, max_tokens, temperature):
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        return None
    r = requests.post(API_URL, headers={"Authorization": "Bearer " + key}, timeout=30,
                      json={"model": "gpt-4o-mini", "max_tokens": max_tokens, "temperature": temperature,
                            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]})
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"].strip()


def generate_blog(topic: str) -> str:
    """Task 3: short blog post about `topic` (max_tokens=100)."""
    text = _call_gpt("You are a helpful blog writer.", "Write a short blog post about: " + topic, 100, 0.7)
    return text or "[offline demo] %s - a quick guide. Looking for the best spots? Start with local favourites, check recent reviews and go at off-peak hours." % topic


def generate_blog_v2(topic: str, tone: str = "friendly and witty", audience: str = "college students") -> str:
    """Task 5: more engaging output via a structured prompt (tone, hook, title, call-to-action)."""
    system = ("You are an engaging blog writer. Always: start with a catchy title, open with a one-line hook, use short "
              "paragraphs, add 3 specific tips, and end with a call-to-action question for the reader.")
    user = "Topic: %s\nTone: %s\nAudience: %s\nLength: about 150 words." % (topic, tone, audience)
    text = _call_gpt(system, user, 300, 0.9)
    return text or ("[offline demo]\n# %s: A Student's Guide\nHook: Your next favourite spot is closer than you think!\n"
                    "Tip 1: Try places with student discounts. Tip 2: Go on weekdays. Tip 3: Ask locals.\nWhere will you go first? Tell us in the comments!" % topic)


if __name__ == "__main__":
    print("--- Task 3 ---\n" + generate_blog("Best Cafes in Ahmedabad"))
    print("\n--- Task 5 (improved) ---\n" + generate_blog_v2("Best Cafes in Ahmedabad"))
