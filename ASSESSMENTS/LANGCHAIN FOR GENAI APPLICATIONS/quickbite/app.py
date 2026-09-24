"""Streamlit QuickBite AI mini-capstone."""
import streamlit as st
from langchain.memory import ConversationBufferMemory
from quickbite.capstone import menu_search, delivery_estimate, respond
st.set_page_config(page_title="QuickBite AI",page_icon="🍽️",layout="centered")
st.title("🍽️ QuickBite AI")
st.caption("Your food delivery companion")
if "messages" not in st.session_state: st.session_state.messages=[]
if "memory" not in st.session_state: st.session_state.memory=ConversationBufferMemory(memory_key="chat_history",input_key="input",return_messages=True)
with st.sidebar:
    st.header("Your preferences")
    address=st.text_input("Delivery address",key="address",placeholder="e.g., 12 River Road, Ahmedabad")
    preference=st.selectbox("Dietary preference",["Any","Vegetarian","Non-vegetarian"],key="preference")
    st.divider(); st.subheader("Delivery estimate")
    distance=st.number_input("Distance (km)",min_value=0.0,value=4.0,step=.5)
    count=st.number_input("Number of items",min_value=1,value=2,step=1)
    rain=st.checkbox("Raining")
    if st.button("Estimate delivery time"):
        st.info(delivery_estimate(distance,count,int(rain)))
    if st.button("Clear Chat",use_container_width=True):
        st.session_state.messages=[]
        st.session_state.memory=ConversationBufferMemory(memory_key="chat_history",input_key="input",return_messages=True)
        st.rerun()
# Session values are injected into every prompt/tool call through respond().
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])
if prompt:=st.chat_input("Ask for a dish or delivery estimate…"):
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"): st.markdown(prompt)
    history="\n".join(f"{m['role']}: {m['content']}" for m in st.session_state.messages[:-1])
    with st.chat_message("assistant"):
        with st.spinner("QuickBite is thinking…"):
            answer=respond(prompt,address or "not provided",preference,history,st.session_state.memory)
        st.markdown(answer)
    st.session_state.messages.append({"role":"assistant","content":answer})
with st.expander("Browse menu"):
    cuisine=st.text_input("Filter cuisine (optional)")
    for item in menu_search(preference,cuisine): st.write(f"**{item['name']}** · {item['cuisine']} · ₹{item['price']} · {'Veg' if item['veg'] else 'Non-veg'}")
