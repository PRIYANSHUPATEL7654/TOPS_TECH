"""B4: Five-turn ConversationChain with memory and clean interactive exit."""
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain_core.language_models.fake import FakeListLLM
from quickbite.llm import configured_chat_model

TEMPLATE="""You are QuickBite's order assistant. Order data: #101 is Preparing, #102 is Out for delivery, #103 is Delivered. Resolve a follow-up like 'What about the other order?' using conversation history. If no ID is specified and none can be resolved, ask for it. If an ID is unknown, say it was not found.
{history}
Human: {input}
Assistant:"""
def main():
    llm=configured_chat_model() or FakeListLLM(responses=["Order #101 is Preparing.","Order #102 is Out for delivery.","#102 is Out for delivery.","Your address is remembered for this session.","I can also help with menu questions.","Please share the order ID."]*20)
    memory=ConversationBufferMemory(memory_key="history",input_key="input",return_messages=False)
    chain=ConversationChain(llm=llm,memory=memory,prompt=PromptTemplate(input_variables=["history","input"],template=TEMPLATE),verbose=False)
    turns=["What is the status of order #101?","What about order #102?","And the other order?","Can you remind me which order was out for delivery?","What else can you help me with?"]
    count=0; seen=set()
    for text in turns:
        answer=chain.predict(input=text); print(f"User: {text}\nQuickBite: {answer}"); count+=1
        import re
        seen.update(re.findall(r"#\d+",text))
    while True:
        try: text=input("User (type exit to stop): ").strip()
        except (EOFError,KeyboardInterrupt): text="exit"
        if text.lower()=="exit": break
        if not text: continue
        answer=chain.predict(input=text); print(f"User: {text}\nQuickBite: {answer}"); count+=1
        import re
        seen.update(re.findall(r"#\d+",text))
    print(f"Total turns: {count}")
    print("Full memory buffer:\n"+str(memory.buffer))
if __name__=="__main__": main()
