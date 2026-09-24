"""Session 4: LangChain conversation memory and custom arithmetic tool."""
import ast,operator,re
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain.agents import AgentExecutor,create_tool_calling_agent
from langchain.memory import ConversationBufferMemory
from quickbite.llm import configured_chat_model
@tool
def calculator(expression:str)->str:
    """Evaluate basic arithmetic with +, -, *, / and parentheses."""
    ops={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv}
    def ev(n):
        if isinstance(n,ast.Constant) and isinstance(n.value,(int,float)):return n.value
        if isinstance(n,ast.BinOp) and type(n.op) in ops:return ops[type(n.op)](ev(n.left),ev(n.right))
        if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):return -ev(n.operand)
        raise ValueError("Unsupported arithmetic")
    return str(ev(ast.parse(expression,mode="eval").body))
def main():
    memory=ConversationBufferMemory(memory_key="chat_history",input_key="input",return_messages=True)
    llm=configured_chat_model(); agent=None
    if llm:
        prompt=ChatPromptTemplate.from_messages([("system","You are a food-order assistant. Remember the restaurant and cuisine the user mentions. Use the calculator tool for calculations; answer normal questions conversationally."),MessagesPlaceholder("chat_history"),("human","{input}"),MessagesPlaceholder("agent_scratchpad")])
        chain=create_tool_calling_agent(llm,[calculator],prompt)
        agent=AgentExecutor(agent=chain,tools=[calculator],memory=memory,verbose=False)
    restaurant=None;cuisine=None
    print("Food-order assistant. Try: I prefer Italian cuisine; restaurant is Olive House. Then ask what you remember. Type exit to stop.")
    while True:
        q=input("You: ").strip()
        if q.lower()=="exit":break
        if not q:continue
        m=re.search(r"restaurant is ([A-Za-z ]+)",q,re.I)
        if m:restaurant=m.group(1).strip()
        m=re.search(r"prefer ([A-Za-z -]+) cuisine",q,re.I)
        if m:cuisine=m.group(1).strip()
        if agent:
            out=agent.invoke({"input":q})["output"]
        elif re.search(r"\d\s*[+*/-]\s*\d",q):
            expr=re.search(r"[\d().+*/ -]+",q).group().strip()
            try:out="Calculator says: "+calculator.invoke({"expression":expr})
            except Exception:out="I couldn't parse that calculation."
            memory.save_context({"input":q},{"output":out})
        else:
            out=f"Got it. I’ll remember restaurant={restaurant or 'not set'} and cuisine={cuisine or 'not set'} for this session."
            memory.save_context({"input":q},{"output":out})
        print("QuickBite:",out)
    print("Conversation turns retained:",len(memory.chat_memory.messages)//2)
if __name__=="__main__":main()
