"""Session 3: friendly contextual CLI bot with follow-up context."""
from quickbite.llm import configured_chat_model,demo_reply
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage,AIMessage
teams={"mumbai indians":"Hardik Pandya","gujarat titans":"Shubman Gill","chennai super kings":"Ruturaj Gaikwad"}
def main():
    llm=configured_chat_model(); history=[]; last_team=None
    print("IPL food-fan chatbot. Type exit to stop.")
    while True:
        q=input("You: ").strip()
        if q.lower()=="exit": break
        ql=q.lower()
        for t in teams:
            if t in ql: last_team=t
        if "captain" in ql and last_team:
            out=f"{teams[last_team]} is the captain of {last_team.title()}. 🏏"
        elif "song" in ql or "playlist" in ql:
            out="🎶 Your match-day playlist: upbeat stadium anthems, big hooks, and one victory song for the innings break!"
        elif llm:
            p=ChatPromptTemplate.from_messages([("system","You are a warm IPL fan chatbot. Keep replies natural, lively, and concise. Use context for follow-ups."),MessagesPlaceholder("history"),("human","{input}")])
            out=llm.invoke(p.format_messages(history=history,input=q)).content
        else: out=demo_reply(q)
        print("Bot:",out); history += [HumanMessage(content=q),AIMessage(content=out)]
if __name__=="__main__": main()
