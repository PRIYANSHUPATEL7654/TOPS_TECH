"""QuickBite capstone logic: filtered menu, delivery tool, few-shot prompt, optional LangChain agent."""
import json
from pathlib import Path
import os, requests
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.memory import ConversationBufferMemory
from .llm import configured_chat_model, demo_reply
ROOT=Path(__file__).resolve().parents[1]
MENU=json.loads((ROOT/"quickbite/menu.json").read_text(encoding="utf-8"))

def menu_search(preference="Any", cuisine=""):
    items=MENU
    p=preference.lower()
    if "veg" in p and "non" not in p: items=[x for x in items if x["veg"]]
    elif "non" in p: items=[x for x in items if not x["veg"]]
    if cuisine.strip():
        found=[x for x in items if cuisine.lower() in x["cuisine"].lower() or cuisine.lower() in x["name"].lower()]
        if found: items=found
    return items[:3]

def delivery_estimate(distance_km,num_items,rain_flag):
    url=os.getenv("DELIVERY_API_URL","http://127.0.0.1:5000/predict")
    try:
        r=requests.post(url,json={"distance_km":distance_km,"num_items":num_items,"rain_flag":rain_flag},timeout=5)
        r.raise_for_status(); return f"Estimated delivery time: {r.json()['predicted_delivery_time_min']:.1f} minutes."
    except requests.RequestException as exc: return f"Delivery estimate unavailable: {exc}. Start the Flask API and try again."

def make_agent(address,preference,memory=None):
    llm=configured_chat_model()
    if llm is None: return None
    @tool
    def get_delivery_estimate(distance_km:float,num_items:int,rain_flag:int)->str:
        """Estimate delivery time. Use when a customer asks how long an order will take. rain_flag is 1 for rain, otherwise 0."""
        return delivery_estimate(distance_km,num_items,rain_flag)
    @tool
    def search_menu(cuisine:str="")->str:
        """Find up to three menu choices matching the customer's dietary preference and an optional cuisine."""
        return json.dumps(menu_search(preference,cuisine))
    prompt=ChatPromptTemplate.from_messages([
      ("system", """You are QuickBite Food Delivery's helpful, concise ordering assistant. Session address: {address}. Dietary preference: {preference}. Follow it carefully. Use tools for menu search and delivery-time estimates. Never invent live estimates. Keep replies friendly and customer-facing.
Few-shot examples:
Customer: Recommend a vegetarian North Indian dish.
QuickBite: Try Paneer Tikka Masala or Dal Makhani—both are comforting North Indian vegetarian favourites.
Customer: How long will 2 items take over 4 km in dry weather?
QuickBite: I’ll check the delivery estimate for that route and order now."""),
      MessagesPlaceholder("chat_history"),("human","{input}"),MessagesPlaceholder("agent_scratchpad")])
    prompt=prompt.partial(address=address or "not provided",preference=preference)
    agent=create_tool_calling_agent(llm,[get_delivery_estimate,search_menu],prompt)
    memory=memory or ConversationBufferMemory(memory_key="chat_history",input_key="input",return_messages=True)
    return AgentExecutor(agent=agent,tools=[get_delivery_estimate,search_menu],memory=memory,verbose=False,handle_parsing_errors=True)

def respond(message,address,preference,history_text="",memory=None):
    if any(k in message.lower() for k in ["recommend","menu","dish","cuisine","food"]):
        cuisine=next((x for x in ["North Indian","South Indian","Italian","Japanese","Indo-Chinese","Hyderabadi"] if x.lower() in message.lower()),"")
        matches=menu_search(preference,cuisine)
        context="; ".join(f"{x['name']} ({x['cuisine']}, ₹{x['price']})" for x in matches) or "No matching dishes found."
    else: context=""
    executor=make_agent(address,preference,memory)
    if executor:
        try: return executor.invoke({"input":f"{message}\nRelevant menu matches (use these for recommendations): {context}" if context else message})["output"]
        except Exception as e: return f"I couldn't reach the language model: {e}"
    if context: return f"Based on your {preference} preference, here are good matches: {context}."
    if "how long" in message.lower() or "delivery time" in message.lower():
        return "Please provide distance in km, item count, and whether it is raining so I can use the delivery estimator."
    return demo_reply(message,history_text)
