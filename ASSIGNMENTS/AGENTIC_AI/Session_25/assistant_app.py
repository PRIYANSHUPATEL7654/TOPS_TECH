"""Streamlit chat UI with keyword intent routing, local memory, and progress status."""
import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Session_24"))
import streamlit as st
from personal_assistant_tools import calculate, motivational_quote

def detect_intent(user_input):
    text=user_input.casefold()
    if any(x in text for x in ("booking","book movie","showtime")): return "show_bookings"
    if any(x in text for x in ("song","music","playlist")): return "play_music"
    if any(x in text for x in ("weather","temperature")): return "get_weather"
    if any(x in text for x in ("quote","motivate")): return "get_quote"
    if any(x in text for x in ("calculate","what is","compute")): return "calculate"
    return "general_help"
def select_tool(intent):
    return {"show_bookings":"Booking lookup (mock)","play_music":"Spotify search (token required)","get_weather":"Open-Meteo weather tool","get_quote":"Sample quote tool","calculate":"Safe calculator"}.get(intent,"Clarification/help")
def respond(text,intent):
    if intent=="get_quote": return motivational_quote()
    if intent=="calculate":
        import re
        expr=re.sub(r"^(what is|calculate|compute)\s+","",text.strip(),flags=re.I).rstrip("?")
        try: return str(calculate(expr))
        except Exception: return "Please enter a math expression using numbers and +, -, *, /, or parentheses."
    if intent=="get_weather": return "Weather tool selected. For a live result, use Session_24/personal_assistant_tools.py with internet access."
    if intent=="play_music": return "Music search selected. Configure a Spotify access token to call the API."
    if intent=="show_bookings": return "Booking lookup selected. No personal bookings are connected in this demo."
    return "I can help with weather, a sample quote, a calculation, music search, or a booking lookup."

st.set_page_config(page_title="Personal Assistant Agent",page_icon="🤖")
st.title("Personal Assistant Agent")
if "history" not in st.session_state: st.session_state.history=[]
for item in st.session_state.history[-3:]:
    with st.chat_message(item["role"]): st.write(item["content"])
user_text=st.chat_input("Ask for weather, music, bookings, a calculation, or a quote")
if user_text:
    st.session_state.history.append({"role":"user","content":user_text})
    intent=detect_intent(user_text); tool=select_tool(intent)
    with st.spinner(f"Understanding request and selecting {tool}…"):
        time.sleep(0.25); answer=respond(user_text,intent)
    st.session_state.history.append({"role":"assistant","content":answer})
    st.rerun()
