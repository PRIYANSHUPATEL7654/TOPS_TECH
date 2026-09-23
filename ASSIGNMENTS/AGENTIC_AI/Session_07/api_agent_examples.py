"""API/local-model exercises. API keys are read from environment variables."""
import os, requests

def gemini_latest_ipl_summary(api_key=None):
    key=api_key or os.getenv("GEMINI_API_KEY")
    if not key: return "Set GEMINI_API_KEY to call Gemini. Ask it for a sourced summary and verify the match date/results before submission."
    url=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={key}"
    prompt="Summarize the latest completed IPL cricket match in 3 sentences. State the date and teams, and say if current match data cannot be verified."
    r=requests.post(url,json={"contents":[{"parts":[{"text":prompt}]}]},timeout=30); r.raise_for_status()
    return r.json()["candidates"][0]["content"]["parts"][0]["text"]

def urgent_alert(messages):
    return ["Alert: Urgent message received!" if "urgent" in m.casefold() else "No urgent messages." for m in messages]

if __name__=="__main__":
    print(gemini_latest_ipl_summary())
    print(*urgent_alert(["Delivery delayed", "Urgent: call me"]),sep="\n")
    print("Restaurant NER demo is in restaurant_ner.py")
