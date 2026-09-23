"""Session 4 revised assignment: Zomato-style search and simple local tools."""
import os,json
from pathlib import Path
from collections import Counter
PLAYLIST=Path(__file__).with_name("my_playlist.txt")
MOCK_RESTAURANTS=[{"name":"Dosa House","cuisines":["South Indian"],"rating":4.5},{"name":"Pizza Corner","cuisines":["Italian","Pizza"],"rating":4.2},{"name":"Green Bowl","cuisines":["Healthy","Vegetarian"],"rating":4.6},{"name":"Dosa Express","cuisines":["South Indian"],"rating":4.1}]
def search_restaurants(query):
    """Use configured Zomato-compatible endpoint; otherwise run transparent mock search."""
    endpoint=os.getenv("ZOMATO_API_URL"); key=os.getenv("ZOMATO_API_KEY")
    if endpoint and key:
        try:
            import requests
            r=requests.get(endpoint,headers={"Authorization":key},params={"q":query},timeout=15); r.raise_for_status(); data=r.json()
            return [x.get("name",x.get("restaurant",{}).get("name","")) for x in data.get("restaurants",[])[:3]]
        except Exception as e: return {"error":f"Configured API request failed: {e}"}
    words=[w.casefold() for w in query.split() if len(w)>2]
    matches=[r["name"] for r in MOCK_RESTAURANTS if any(w in (r["name"]+" "+" ".join(r["cuisines"])).casefold() for w in words)]
    return matches[:3]

def suggest_from_playlist(path=PLAYLIST):
    lines=[x.strip() for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
    artists=Counter(x.split(" - ",1)[1] for x in lines if " - " in x)
    artist=artists.most_common(1)[0][0] if artists else "Unknown Artist"
    return f"Based on your most common artist ({artist}), try a new song by {artist}."

def movie_prompt_chain(preference,location):
    home=input("Do you prefer Hollywood or Bollywood? ").strip().casefold()
    industry="Hollywood" if home.startswith("h") else "Bollywood"
    return f"For {preference} fans preferring {industry}, try a popular {industry} {preference} film. (Location noted: {location or 'not provided'}.)"

def plan_weekend_trip():
    steps=["Find train or flight tickets","Book accommodation","Suggest sightseeing spots"]
    for number,step in enumerate(steps,1): print(f"{number}. {step}")
    return steps

MEMORY={}
def record_search(query,result,memory=MEMORY):
    memory["last_search"]={"query":query,"result":result}; print("Updated search memory:",json.dumps(memory,indent=2)); return memory

if __name__=="__main__":
    query=input("Restaurant query (example: best pizza near me): "); result=search_restaurants(query); print("Input → API/mock search → results:",query,"→",result)
    print(suggest_from_playlist()); print(movie_prompt_chain("action","Ahmedabad")); plan_weekend_trip(); record_search(query,result)
