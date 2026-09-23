"""LangGraph city-first recommendation workflow, using a fixed safe sample catalog."""
from typing import TypedDict
from langgraph.graph import StateGraph,START,END
CATALOG={"Ahmedabad":["Agashiye","Swati Snacks","The Green House"],"Mumbai":["Soam","Trishna","The Bombay Canteen"]}
class State(TypedDict): city:str; restaurants:list[str]
def ask_city(state): return {"city":input("Which city? ").strip().title()}
def recommend(state): return {"restaurants":CATALOG.get(state["city"],[])}
def present(state):
    names=state.get("restaurants",[])
    print("Suggestions:",", ".join(names) if names else "No sample list for this city.")
    return {}
g=StateGraph(State); g.add_node("ask_city",ask_city);g.add_node("recommend",recommend);g.add_node("present",present);g.add_edge(START,"ask_city");g.add_edge("ask_city","recommend");g.add_edge("recommend","present");g.add_edge("present",END);app=g.compile()
if __name__=="__main__":app.invoke({"city":"","restaurants":[]})
