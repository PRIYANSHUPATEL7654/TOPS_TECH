"""LangChain Runnable over a mock trends tool; prints top two trends."""
from langchain_core.runnables import RunnableLambda
MOCK=[{"name":"#AgenticAI","posts":840},{"name":"#Cricket","posts":1200},{"name":"#Python","posts":990}]
def fetch_and_summarize(_): return sorted(MOCK,key=lambda x:x["posts"],reverse=True)[:2]
trend_chain=RunnableLambda(fetch_and_summarize)
if __name__=="__main__":
    print("Mock trend summary:")
    for t in trend_chain.invoke(None):print(f"{t['name']}: {t['posts']} sample posts")
