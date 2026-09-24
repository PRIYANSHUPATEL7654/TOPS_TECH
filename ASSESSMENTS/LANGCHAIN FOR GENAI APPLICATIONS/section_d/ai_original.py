"""AI-generated first draft, intentionally preserved with a memory-key bug for Section D."""
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain_core.language_models.fake import FakeListLLM
orders={"#101":"Preparing","#102":"Out for delivery"}
# BUG: memory_key is 'chat_history' but the prompt expects {history}; this can raise a missing-variable error.
memory=ConversationBufferMemory(memory_key="chat_history",input_key="input")
prompt=PromptTemplate(input_variables=["history","input"],template="Order status helper.\n{history}\nHuman: {input}\nAssistant:")
chain=ConversationChain(llm=FakeListLLM(responses=["Order is preparing."]*10),memory=memory,prompt=prompt)
while True:
    q=input("Ask: ")
    if q.lower()=="quit": break
    print(chain.predict(input=q))
print("Done")
