"""Advanced agent exercises: tool, plan, playlist policy, PDF and ticket extraction."""
import re
from pathlib import Path
def call_weather_api(city):
    temps={"Ahmedabad":31,"Mumbai":29,"Delhi":27}
    return {"city":city,"temperature_c":temps.get(city.title()),"source":"mock"}
def food_order_plan(restaurant, items):
    return ["1. Recommend a restaurant matching the user's preferences.","2. Show current menu and prices.",f"3. Add requested items ({', '.join(items)}) to a draft cart.","4. Show total and delivery details.","5. Ask for explicit confirmation before placing the order."]
def decide_playlist_action(song_likes, song_skips):
    if song_skips>=5: return "remove_candidate"
    if song_likes>=10: return "promote_song"
    return "recommend_song"
def extract_ticket_fields(text):
    patterns={"movie":r"Movie\s*:\s*(.+)","seat":r"Seat\s*:\s*(.+)","showtime":r"Showtime\s*:\s*(.+)"}
    return {k:(re.search(p,text,re.I).group(1).strip() if re.search(p,text,re.I) else None) for k,p in patterns.items()}
if __name__=="__main__":
    print(call_weather_api("Ahmedabad")); print(*food_order_plan("Sample",["Dosa"]),sep="\n")
    print(decide_playlist_action(11,1)); print(extract_ticket_fields("Movie: Example Film\nSeat: B12\nShowtime: 7:30 PM"))
