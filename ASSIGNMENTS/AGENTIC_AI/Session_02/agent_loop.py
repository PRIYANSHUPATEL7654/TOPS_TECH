"""Small deterministic perceive -> think -> act example; standard library only."""
import re

APP_NAMES = ("spotify", "bookmyshow", "youtube")
INTENTS = ("show", "play", "book", "search", "find")

def perceive_input(message: str) -> dict:
    text = message.strip()
    words = re.findall(r"[\w'-]+", text.lower())
    intent = next((word for word in words if word in INTENTS), "unknown")
    app = next((name for name in APP_NAMES if name in text.lower()), None)
    return {"text": text, "intent": intent, "app": app, "keywords": [w for w in words if w not in INTENTS and w != app]}

def decide_next_action(perceived_data: dict) -> str:
    intent, app = perceived_data["intent"], perceived_data["app"]
    if intent == "show" and app == "spotify": return "fetch_spotify_trending"
    if intent in {"search", "find"} and app == "bookmyshow": return "search_movie_bookmyshow"
    if intent == "play" and app == "youtube": return "search_youtube_video"
    return "ask_for_clarification"

def execute_action(action: str) -> str:
    mock = {
        "fetch_spotify_trending": "Fetching trending songs from Spotify… (mock result: 3 songs)",
        "search_movie_bookmyshow": "Searching movies on BookMyShow… (mock result: 2 titles)",
        "search_youtube_video": "Searching YouTube… (mock result: 1 video)",
        "ask_for_clarification": "Please mention an action and a supported app (Spotify, BookMyShow, or YouTube).",
    }
    return mock[action]

if __name__ == "__main__":
    request = input("What would you like me to do? ")
    parsed = perceive_input(request)
    action = decide_next_action(parsed)
    print("Perceived:", parsed)
    print("Action:", action)
    print(execute_action(action))
