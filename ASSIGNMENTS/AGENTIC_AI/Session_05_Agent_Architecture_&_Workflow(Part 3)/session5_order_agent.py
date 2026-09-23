"""Session 5 revised assignment: booking workflow, state machine and safety."""
from pathlib import Path
import json
STATES=("Browsing","Adding to Cart","Payment","Order Placed")
TRANSITIONS={"Browsing":{"choose":"Adding to Cart"},"Adding to Cart":{"add":"Adding to Cart","checkout":"Payment","back":"Browsing"},"Payment":{"paid":"Order Placed","cancel":"Adding to Cart"},"Order Placed":{}}
def order_machine(actions):
    state="Browsing"; print(state)
    for action in actions:
        next_state=TRANSITIONS[state].get(action)
        if not next_state: print("Rejected transition:",action,"from",state); continue
        state=next_state; print(state)
    return state

def pizza_plan(request,open_places):
    steps=["Parse pizza intent and location","Find nearby pizza restaurants","Check today's opening hours","Return open options or ask for another time"]
    for i,s in enumerate(steps,1): print(f"Step {i}: {s}")
    candidates=[p for p in open_places if p["open"]]
    return {"request":request,"open_now":candidates}

def bounded_agent(next_action,max_steps=5):
    for i in range(1,max_steps+1):
        result=next_action(); print(f"Iteration {i}: {result}")
        if result.get("done"): return "Completed"
    return f"Stopped after maximum of {max_steps} iterations."

def flipkart_wishlist(action,item,price,approved=False):
    if action=="add" and price>50000 and not approved: return "Blocked: expensive item requires confirmation."
    if action not in {"add","remove"}: return "Blocked: unsupported wishlist action."
    return f"{'Added' if action=='add' else 'Removed'} {item} in wishlist."

if __name__=="__main__":
    order_machine(["choose","add","checkout","paid"])
    print(pizza_plan("Find pizza nearby and check open now",[{"name":"Pizza One","open":True},{"name":"Pizza Two","open":False}]))
    count=0
    def action():
        global count
        count+=1; return {"done":count==8,"status":"pending"}
    print(bounded_agent(action)); print(flipkart_wishlist("add","Laptop",75000)); print(flipkart_wishlist("add","Laptop",75000,approved=True))
