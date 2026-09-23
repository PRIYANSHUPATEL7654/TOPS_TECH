"""Session 3 revised assignment: agent loop and memory exercises."""
from collections import Counter, deque

SONGS=[{"title":"Sunrise Drive","artist":"Asha","genre":"Pop"},{"title":"Soft Rain","artist":"Asha","genre":"Jazz"},{"title":"Blue Sky","artist":"Ravi","genre":"Pop"}]

def perceive(last_song): return next((s for s in SONGS if s["title"].casefold()==last_song.casefold()),None)
def think(song): return (song["genre"], next((s for s in SONGS if s["genre"]==song["genre"] and s["title"]!=song["title"]),SONGS[0])) if song else ("Pop",SONGS[0])
def act(choice): return f"Suggested: {choice['title']} by {choice['artist']}"
def learn(preferences, genre): preferences[genre]=preferences.get(genre,0)+1; return preferences

def music_agent(last_played, preferences=None):
    preferences=preferences if preferences is not None else {}
    song=perceive(last_played); print("Perceive:",song or "unknown track")
    genre,choice=think(song); print("Think: prefer another",genre,"track")
    result=act(choice); print("Act:",result); print("Learn:",learn(preferences,genre)); return result

class ShortTermMemory:
    def __init__(self, capacity=5): self._messages=deque(maxlen=capacity)
    def add_message(self,message): self._messages.append(str(message))
    def get_memory(self): return list(self._messages)

def add_preference(memory,user_id,key,value): memory.setdefault(user_id,{})[key]=value; return memory[user_id]
def get_preferences(memory,user_id): return memory.get(user_id,{})

if __name__=="__main__":
    music_agent("Sunrise Drive")
    print("Food delivery loop: Perceive dietary need and address; Think check item/store/time; Act query menu or draft cart; Learn update preference after feedback.")
    stm=ShortTermMemory(); [stm.add_message(x) for x in ["Hi","Need dinner","Vegetarian","Under $300","Ahmedabad","No onion"]]; print("Last 5 messages:",stm.get_memory())
    long={}; add_preference(long,"user-7","favorite_cuisine","Gujarati"); add_preference(long,"user-7","payment_method","UPI"); print("user-7:",get_preferences(long,"user-7"))
