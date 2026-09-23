"""Deterministic conversational Q&A over provided IPL teams/captains."""
TEAMS={"Mumbai Indians":"Hardik Pandya","Chennai Super Kings":"Ruturaj Gaikwad","Royal Challengers Bengaluru":"Rajat Patidar","Kolkata Knight Riders":"Ajinkya Rahane"}
def answer(question):
    q=question.casefold()
    for team,captain in TEAMS.items():
        if team.casefold() in q:return f"{captain} is listed as captain of {team} in this sample dataset."
    return "I can answer only about the teams in the supplied sample list: "+", ".join(TEAMS)
if __name__=="__main__":
    while True:
        q=input("Ask (or quit): ")
        if q.casefold()=="quit":break
        print(answer(q))
