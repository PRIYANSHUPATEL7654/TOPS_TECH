"""OMDb movie lookup, menu CSV search, SQLite song lookup, and prompt-chain demo."""
import csv, os, sqlite3
from pathlib import Path
try:
    import requests
except ImportError:
    class _RequestsUnavailable:
        class RequestException(Exception): pass
        @staticmethod
        def get(*args, **kwargs): raise RuntimeError("Install requests: python -m pip install requests")
        @staticmethod
        def post(*args, **kwargs): raise RuntimeError("Install requests: python -m pip install requests")
    requests = _RequestsUnavailable()
HERE=Path(__file__).parent

def find_movie(title, api_key=None):
    key=api_key or os.getenv("OMDB_API_KEY")
    if not key: return {"error":"Set OMDB_API_KEY to use OMDb; sample result mode is available in the command line."}
    response=requests.get("https://www.omdbapi.com/",params={"apikey":key,"t":title,"plot":"short"},timeout=20)
    response.raise_for_status(); data=response.json()
    if data.get("Response")=="False": return {"error":data.get("Error","Movie not found")}
    return {"title":data.get("Title"),"year":data.get("Year"),"imdb_rating":data.get("imdbRating"),"plot":data.get("Plot")}

def menu_search(cuisine, file=HERE/"menu.csv"):
    with open(file, newline="", encoding="utf-8") as f:
        return [row for row in csv.DictReader(f) if row["cuisine"].casefold()==cuisine.casefold()]

def init_songs_db(db=HERE/"music.db"):
    with sqlite3.connect(db) as con:
        con.execute("CREATE TABLE IF NOT EXISTS songs (name TEXT PRIMARY KEY, artist TEXT NOT NULL)")
        con.executemany("INSERT OR IGNORE INTO songs VALUES (?,?)",[("Blinding Lights","The Weeknd"),("Kesariya","Arijit Singh")])

def song_exists(name, db=HERE/"music.db"):
    init_songs_db(db)
    with sqlite3.connect(db) as con: return con.execute("SELECT 1 FROM songs WHERE name=? COLLATE NOCASE",(name,)).fetchone() is not None

def search_movies(query, api_key=None):
    key=api_key or os.getenv("OMDB_API_KEY")
    if not key: return {"error":"Set OMDB_API_KEY to search OMDb."}
    response=requests.get("https://www.omdbapi.com/",params={"apikey":key,"s":query,"type":"movie"},timeout=20)
    response.raise_for_status(); data=response.json()
    if data.get("Response")=="False": return {"error":data.get("Error","No movies found")}
    return data.get("Search",[])

def movie_prompt_chain(genre):
    """Ask for a genre, search candidate titles, then fetch one title's full details."""
    candidates=search_movies(genre)
    if isinstance(candidates,dict) and "error" in candidates: return candidates["error"]
    print("Matches:",[(m.get("Title"),m.get("Year")) for m in candidates[:3]])
    choice=input("Pick a movie title for details: ").strip()
    return find_movie(choice)

if __name__=="__main__":
    title=input("Movie title for OMDb (blank for sample): ").strip()
    if title:
        try: print(find_movie(title))
        except requests.RequestException as exc: print("Network/API error:",exc)
    else: print({"title":"Example Movie","year":"2024","imdb_rating":"7.2"})
    cuisine=input("Cuisine to search (e.g. Italian): ").strip()
    print("Matches:",menu_search(cuisine))
    name=input("Song title to check: ").strip()
    print("Song found" if song_exists(name) else "Song not found")
