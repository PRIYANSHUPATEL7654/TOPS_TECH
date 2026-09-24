"""B3 Streamlit promotional dish-description generator."""
import os, requests, streamlit as st
from quickbite.llm import configured_chat_model
st.set_page_config(page_title="QuickBite Dish Copy",page_icon="🥘")
st.title("🥘 Dish Description Generator")
name=st.text_input("Dish Name",placeholder="Paneer Tikka Masala")
cuisine=st.text_input("Cuisine Type",placeholder="North Indian")
length=st.selectbox("Description Length",["Short","Medium","Long"])
def generate():
    prompt=(f"Write a {length.lower()} promotional description for {name}, a {cuisine} dish. "
            "Use an appetising, customer-facing tone. Describe only plausible qualities; do not invent allergens or health claims.")
    print("FINAL PROMPT:\n"+prompt)
    # Store the exact request so Regenerate does not require re-entering the fields.
    st.session_state["last_prompt"]=prompt
    llm=configured_chat_model()
    if llm:
        try: return llm.invoke(prompt).content
        except Exception as exc: return f"Model request failed: {exc}"
    base=f"Savour {name}, a {cuisine} favourite prepared with aromatic spices and a rich, comforting finish."
    return base if length=="Short" else base+" Each bite brings together bold flavour and satisfying texture—an inviting choice for your next meal."
if st.button("Generate description",type="primary",disabled=not(name.strip() and cuisine.strip())) or st.session_state.get("regenerate"):
    st.session_state["regenerate"]=False
    with st.spinner("Generating description…"):
        result=generate()
    st.session_state["description"]=result
if "description" in st.session_state:
    with st.container(border=True): st.write(st.session_state["description"])
    st.caption(f"Character count: {len(st.session_state['description'])}")
    if st.button("Regenerate"):
        st.session_state["regenerate"]=True; st.rerun()
