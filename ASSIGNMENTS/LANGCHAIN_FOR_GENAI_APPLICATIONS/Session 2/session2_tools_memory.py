"""Session 2: LangChain tools + tool-calling agent + memory; mock catalog fallback."""
import ast,operator
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain.agents import AgentExecutor,create_tool_calling_agent
from langchain.memory import ConversationBufferMemory
from quickbite.llm import configured_chat_model
TEAMS={"Mumbai Indians":"Hardik Pandya","Gujarat Titans":"Shubman Gill","Chennai Super Kings":"Ruturaj Gaikwad"}
MOVIES=["Example Film A","Example Film B","Example Film C"]
@tool
def calculator(expression:str)->str:
    """Calculate a basic arithmetic expression with +, -, *, / and parentheses."""
    ops={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv}
    def ev(n):
        if isinstance(n,ast.Constant) and isinstance(n.value,(int,float)): return n.value
        if isinstance(n,ast.BinOp) and type(n.op) in ops: return ops[type(n.op)](ev(n.left),ev(n.right))
        raise ValueError("Only basic arithmetic is allowed")
    return str(ev(ast.parse(expression,mode="eval").body))
@tool
def search_catalog(query:str)->str:
    """Search the local mock catalog for IPL captains or trending mock movies."""
    q=query.lower()
    for team,captain in TEAMS.items():
        if team.lower() in q:return f"{team} captain: {captain}"
    if "movie" in q or "film" in q:return "Mock trending movies: "+", ".join(MOVIES)
    return "No matching mock catalog records. Try an IPL team or trending movies."
def main():
    llm=configured_chat_model()
    tools=[calculator,search_catalog]
    memory=ConversationBufferMemory(memory_key="chat_history",input_key="input",return_messages=True)
    if llm:
        prompt=ChatPromptTemplate.from_messages([("system","Answer questions about IPL teams and mock trending movies. Use calculator for arithmetic, catalog tool for team/movie facts. Be concise."),MessagesPlaceholder("chat_history"),("human","{input}"),MessagesPlaceholder("agent_scratchpad")])
        agent=create_tool_calling_agent(llm,tools,prompt)
        executor=AgentExecutor(agent=agent,tools=tools,memory=memory,verbose=False)
        while True:
            q=input("You (exit to stop): ").strip()
            if q.lower()=="exit":break
            if q: print("Agent:",executor.invoke({"input":q})["output"])
    else:
        # Offline deterministic equivalent keeps exercises testable without a model API.
        for q in ["My name is Priyanshu","Who is Gujarat Titans captain?","What is 12 times 8?","Show trending movies"]:
            if "times" in q: ans=calculator.invoke({"expression":"12*8"})
            else: ans=search_catalog.invoke({"query":q})
            memory.save_context({"input":q},{"output":ans}); print("User:",q,"| Agent:",ans)
        print("Memory retained turns:",len(memory.chat_memory.messages)//2)
if __name__=="__main__":main()
