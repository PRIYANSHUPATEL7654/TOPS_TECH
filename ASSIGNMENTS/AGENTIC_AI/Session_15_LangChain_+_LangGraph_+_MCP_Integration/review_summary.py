"""LangChain Runnable-based review summary without paid model access."""
from langchain_core.runnables import RunnableLambda

def summarize_review(review):
    words=review.split()
    return " ".join(words[:24])+ ("…" if len(words)>24 else "")
summary_chain=RunnableLambda(summarize_review)
if __name__=="__main__":
    review="The phone case arrived quickly, but the box was damaged and the color is slightly different from the photo. The seller replaced it after I contacted support."
    print("Original review:",review); print("Summary:",summary_chain.invoke(review))
