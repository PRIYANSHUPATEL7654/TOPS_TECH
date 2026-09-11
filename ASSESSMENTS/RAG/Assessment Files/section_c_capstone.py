import datetime, re, numpy as np
from sentence_transformers import SentenceTransformer
import faiss
POLICY="Customers can request a refund for missing, incorrect, or damaged items within 24 hours of delivery. The support team verifies the order, restaurant record, and evidence before approving a refund. Approved amounts are returned to the original payment method. Delivery estimates are normally 30 to 45 minutes, but the live estimate shown at checkout takes priority. Customers can cancel before restaurant acceptance without a cancellation charge. After acceptance, preparation may have started and the full item charge may apply. Customers should report late delivery through Help with the order ID. If an item is unavailable, the restaurant may suggest a substitution and the customer can accept or decline it. If the customer declines, the unavailable item is removed from the bill. Support can help with payment failures, address corrections, damaged packaging, and account questions. Refunds are not automatic when a customer simply changes their mind after preparation has begun. All complaints are reviewed against the order record and current policy. The platform stores support interactions for service improvement, safety, fraud prevention, and dispute resolution. Customers should never share a password or one-time passcode with a support representative."
examples=[('My order arrived late','Late Delivery'),('The restaurant sent pasta instead of pizza','Wrong Item'),('My drink was missing','Missing Item'),('The meal was cold and stale','Poor Quality')]
model=SentenceTransformer('all-MiniLM-L6-v2'); words=POLICY.split(); chunks=[' '.join(words[i:i+100]) for i in range(0,len(words),80)]; vec=model.encode(chunks,convert_to_numpy=True).astype('float32'); index=faiss.IndexFlatL2(vec.shape[1]); index.add(vec)
def log(mode,query,output):
    with open('session_log.txt','a',encoding='utf8') as f: f.write(f'{datetime.datetime.now().isoformat()} | {mode} | {query} | {output}\n')
def rag_prompt(q,contexts): return 'Role: policy assistant\n'+'\n'.join(f'{i+1}. {c}' for i,c in enumerate(contexts))+f'\nQuestion: {q}\nAnswer only from context; say I do not know if missing.'
def classify(text):
    q=model.encode([text],convert_to_numpy=True).astype('float32'); e=model.encode([x[0] for x in examples],convert_to_numpy=True).astype('float32'); d=((e-q)**2).sum(axis=1); i=int(np.argmin(d)); return examples[i][1],examples[i][0]
def main():
    asked=classified=0
    while True:
        print('\n1. Ask policy question\n2. Classify complaint\n3. Exit'); choice=input('Choose: ').strip()
        if choice=='3': print(f'Session summary: {asked} policy questions, {classified} complaints classified.'); return
        if choice=='1':
            q=input('Question: ').strip()
            if not q: print('Question cannot be empty.'); continue
            asked+=1; qe=model.encode([q],convert_to_numpy=True).astype('float32'); d,ids=index.search(qe,min(3,index.ntotal)); ctx=[chunks[i] for i in ids[0]]; prompt=rag_prompt(q,ctx); print('Retrieved context:',ctx); print('Prompt:',prompt); out='Simulated answer: the answer must be checked against the retrieved policy context.'; print(out); log('RAG',q,out)
        elif choice=='2':
            q=input('Complaint: ').strip()
            if not q: print('Complaint cannot be blank.'); continue
            classified+=1; label,near=classify(q); out=f'{label}; closest example: {near}'; print(out); log('Classify',q,out)
        else: print('Choose 1, 2, or 3.')
if __name__=='__main__': main()
