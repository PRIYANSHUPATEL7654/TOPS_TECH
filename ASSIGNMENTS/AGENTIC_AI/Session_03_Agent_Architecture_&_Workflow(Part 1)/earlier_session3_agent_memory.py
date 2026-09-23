"""Perceive-think-act-learn and three small memory patterns."""
from pathlib import Path
import json
HISTORY = Path(__file__).with_name("play_history.json")

def recommend_restaurant(preference, feedback=None):
    kinds = {"spicy": "Gujarati thali", "light": "South Indian", "vegetarian": "vegetarian cafe"}
    if feedback and feedback.lower() == "too spicy": return "mild vegetarian cafe"
    return kinds.get(preference.lower(), "family restaurant")

def remember_last_three(messages, new_message):
    messages.append(new_message)
    del messages[:-3]
    return messages

def add_played_song(song, path=HISTORY):
    history = json.loads(path.read_text()) if path.exists() else []
    history.append(song)
    path.write_text(json.dumps(history, indent=2), encoding="utf-8")
    return history

def contextual_movie_recommendation(last_movie, movies):
    genre = movies.get(last_movie, {}).get("genre")
    if not genre: return "I could not find that movie in the watch history."
    similar = [title for title, details in movies.items() if title != last_movie and details.get("genre") == genre]
    return f"You watched {last_movie} ({genre}); try {', '.join(similar) or 'another ' + genre + ' film'}."

if __name__ == "__main__":
    msgs=[]
    for text in ["hello", "show comedy", "one more"]: print(remember_last_three(msgs,text))
    print("Playlist history:", add_played_song("Sample Song — Example Artist"))
    watched={"The Intern":{"genre":"comedy"},"Free Guy":{"genre":"comedy"},"Arrival":{"genre":"science fiction"}}
    print(contextual_movie_recommendation("The Intern",watched))
