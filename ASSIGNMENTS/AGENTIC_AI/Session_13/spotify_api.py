"""Spotify Web API song search (requires a user-created access token)."""
import os, requests
def fetch_song_info(song_name, token=None):
    token=token or os.getenv("SPOTIFY_ACCESS_TOKEN")
    if not token: return {"error":"Set SPOTIFY_ACCESS_TOKEN; see USER_ACTIONS.txt for setup."}
    r=requests.get("https://api.spotify.com/v1/search",headers={"Authorization":f"Bearer {token}"},params={"q":song_name,"type":"track","limit":1},timeout=20)
    r.raise_for_status(); items=r.json().get("tracks",{}).get("items",[])
    if not items: return {"error":"No matching track found."}
    track=items[0]; return {"title":track["name"],"artist":track["artists"][0]["name"],"album":track["album"]["name"]}
if __name__=="__main__": print(fetch_song_info(input("Song: ")))
