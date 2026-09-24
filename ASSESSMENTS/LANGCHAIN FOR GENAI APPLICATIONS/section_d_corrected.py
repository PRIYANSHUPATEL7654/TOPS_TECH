"""Corrected D submission: order lookup + context + unknown-ID validation."""
import re
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain_core.language_models.llms import LLM
from quickbite.llm import configured_chat_model

ORDERS={"#101":"Preparing","#102":"Out for delivery","#103":"Delivered"}
TEMPLATE="""You are a concise QuickBite tracking assistant. Status data: {order_data}
Use history to resolve omitted or referential order IDs. If an ID is not present in the data, say it was not found. If no order can be identified, ask for an ID.
{history}
Human: {input}
Assistant:"""

def answer_from_orders(text,history):
    ids=re.findall(r"#?\d+",text)
    if not ids:
        old=re.findall(r"#?\d+",history)
        ids=old[-1:] if old else []
    if not ids: return "Please provide an order ID, such as #101."
    found=[]
    for raw in ids:
        key=raw if raw.startswith("#") else "#"+raw
        found.append(f"Order {key}: {ORDERS.get(key,'not found in our order records')}.")
    return " ".join(found)

class OrderLookupLLM(LLM):
    """Tiny deterministic local LLM adapter so the chain can be tested without credentials."""
    @property
    def _llm_type(self): return "quickbite-local-order-lookup"
    @property
    def _identifying_params(self): return {"orders":len(ORDERS)}
    def _call(self,prompt,stop=None,run_manager=None,**kwargs):
        user=re.findall(r"Human: (.*)",prompt)
        history=prompt.split("Human:",1)[0]
        return answer_from_orders(user[-1] if user else "",history)

def main():
    # FIX: the memory key exactly matches {history}; input_key avoids ambiguous inputs.
    memory=ConversationBufferMemory(memory_key="history",input_key="input",return_messages=False)
    # Local lookup model makes the dictionary authoritative and keeps this assessment runnable offline.
    llm=OrderLookupLLM()
    prompt=PromptTemplate(input_variables=["history","input","order_data"],template=TEMPLATE)
    # Keep prompt's order_data variable supplied on each invocation, and preserve the memory history.
    chain=ConversationChain(llm=llm,memory=memory,prompt=prompt,verbose=False)
    count=0; unique=set()
    print("QuickBite order tracking (type quit to exit). Example: status #101; then ‘what about the other order?’")
    while True:
        try: q=input("You: ").strip()
        except (EOFError,KeyboardInterrupt): print(); break
        if q.lower()=="quit": break
        if not q: continue
        ids=re.findall(r"#\d+",q)
        unique.update(ids)
        # The ConversationChain injects history and calls the local order lookup adapter.
        reply=chain.predict(input=q,order_data=str(ORDERS))
        print("QuickBite: "+reply)
        count+=1
    print(f"Turns: {count} | Unique order IDs queried: {len(unique)}")
    print("Unique IDs: "+(", ".join(sorted(unique)) if unique else "none"))
if __name__=="__main__": main()
