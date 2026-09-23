"""Three cooperative workflows with explicit handoffs between functions."""
def fetch_menu(request): return {"restaurant":request.get("restaurant","Sample Kitchen"),"items":[{"name":"Veg thali","price":220},{"name":"Paneer wrap","price":160}]}
def analyze_order(menu, request):
    wanted=request.get("items",["Veg thali"]); selected=[i for i in menu["items"] if i["name"] in wanted]
    return {"restaurant":menu["restaurant"],"selected":selected,"total":sum(i["price"] for i in selected)}
def generate_delivery_report(order): return {"restaurant":order["restaurant"],"items":[i["name"] for i in order["selected"]],"total_inr":order["total"],"status":"Awaiting customer confirmation"}
def trending_agent(playlist): return playlist
def genre_agent(songs): return {"songs":songs,"pop_count":sum(s["genre"].casefold()=="pop" for s in songs)}
def match_agent(scores): return scores
def highest_agent(scores): return {"scores":scores,"leader":max(scores,key=scores.get)}
def report_agent(result): return f"IPL score summary: {result['leader']} lead with {result['scores'][result['leader']]} runs."
if __name__=="__main__":
    request={"restaurant":"Sample Kitchen","items":["Veg thali"]}
    menu=fetch_menu(request); order=analyze_order(menu,request); print(generate_delivery_report(order))
    playlist=trending_agent([{"title":"Song A","genre":"Pop"},{"title":"Song B","genre":"Rock"}]); print(genre_agent(playlist))
    scores=match_agent({"Team A":184,"Team B":176}); print(report_agent(highest_agent(scores)))
