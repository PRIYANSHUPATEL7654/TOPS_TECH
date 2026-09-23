"""Public rationale + action demo. Does not print hidden chain-of-thought."""
def food_delivery_agent(user_input):
    text=user_input.casefold()
    if "menu" in text: action="show_menu"; rationale="The user is asking to see available food options."
    elif "confirm" in text or "order" in text: action="request_order_details"; rationale="An order needs item and delivery details, and submission requires confirmation."
    else: action="suggest_restaurant"; rationale="The request is broad, so a restaurant suggestion is a useful first step."
    print("Brief rationale:",rationale)
    print("Action:",action)
    return {"rationale":rationale,"action":action}
def cricket_react_assistant(question):
    # ReAct-style public trace: reason summary -> action -> observation -> answer.
    scores={"Team A":"won by 8 runs", "Team B":"lost by 8 runs"}
    print("Reason summary: The question asks for the result of the last sample match.")
    print("Action: look up the latest match in the local sample score table")
    observation=scores
    print("Observation:",observation)
    if "team a" in question.casefold(): return observation["Team A"]
    if "team b" in question.casefold(): return observation["Team B"]
    return "The sample score table shows Team A won by 8 runs."

if __name__=="__main__":
    food_delivery_agent(input("How can I help? "))
    print(cricket_react_assistant("Who won the last IPL match?"))
