from pathlib import Path
import re

DATA=Path(__file__).with_name("ipl_stats.txt")
STOP={"what","was","the","who","did","in","of","and","tell","me","about","how","many","which"}
def retrieve(question, path=DATA, k=3):
    q={w for w in re.findall(r"[a-z0-9]+",question.lower()) if w not in STOP}
    scored=[]
    for line in path.read_text(encoding="utf-8").splitlines():
        terms=set(re.findall(r"[a-z0-9]+",line.lower()))
        score=len(q & terms)
        if score: scored.append((score,line))
    return [line for _,line in sorted(scored,key=lambda x:(-x[0],x[1]))[:k]]

def answer(question):
    hits=retrieve(question)
    if not hits: return "No matching fact was found in the supplied IPL notes."
    return "Based on the retrieved notes: " + " ".join(hits)

if __name__=="__main__":
    q=input("Ask about the supplied IPL notes: ")
    print(answer(q))
