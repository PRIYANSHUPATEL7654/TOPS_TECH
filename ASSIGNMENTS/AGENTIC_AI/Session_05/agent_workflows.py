"""State machine, multi-hop lookup, bounded loop, and order safety example."""
TICKET={"Start":{"select_match":"Select Match"},"Select Match":{"choose_seats":"Choose Seats"},"Choose Seats":{"pay":"Payment"},"Payment":{"confirm":"Confirmation"},"Confirmation":{}}
def simulate_ticket(actions=("select_match","choose_seats","pay","confirm")):
    state="Start"; print(state)
    for action in actions:
        state=TICKET[state].get(action,"Start")
        print(state)
        if state=="Start": break
    return state

def multi_hop(movie, release_years, songs_by_year):
    year=release_years.get(movie)
    return {"movie":movie,"year":year,"trending_song":songs_by_year.get(year,"Unknown")} if year else {"movie":movie,"error":"Movie not in lookup"}

def bounded_agent(next_step, max_steps=5):
    for step in range(1,max_steps+1):
        result=next_step(step)
        print(f"Step {step}: {result}")
        if result.get("done"): return "Completed"
    return f"Stopped safely after {max_steps} steps."

def safe_food_order(restaurant, dishes, confirmed=False):
    if not restaurant or not dishes: return "Collect restaurant and dish choices first."
    if not confirmed: return f"Prepared {restaurant}: {', '.join(dishes)}. Ask the user to confirm before placing the order."
    return "Order submitted after explicit user confirmation."

if __name__=="__main__":
    print("Ticket ends in:",simulate_ticket())
    print(multi_hop("Example Film",{"Example Film":2023},{2023:"Example Hit"}))
    print(bounded_agent(lambda i:{"done":i==8,"observation":"working"}))
    print(safe_food_order("Example Restaurant",["Veg thali"]))
