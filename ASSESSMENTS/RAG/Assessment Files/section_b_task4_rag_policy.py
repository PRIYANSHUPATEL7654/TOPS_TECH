import re, numpy as np, faiss
from sentence_transformers import SentenceTransformer
POLICY = "Refunds are available for missing or incorrect items when the customer reports the problem within 24 hours. Support verifies the order and may request a photograph. Approved refunds return to the original payment method. Delivery normally occurs within 30 to 45 minutes, although restaurants may display a different estimate. Customers can cancel without charge before the restaurant accepts the order. After acceptance, cancellation may incur the full item charge because preparation may have started. Late deliveries should be reported through Help with the order ID. The support team reviews delays, substitutions, damaged packaging, and quality complaints. Item substitutions require customer approval when the restaurant cannot provide the selected dish. If no replacement is accepted, the unavailable item is removed from the bill. Refund decisions are based on order records and the current policy."
def chunk(text, size=100, overlap=20):
    words=text.split(); step=size-overlap; return [' '.join(words[i:i+size]) for i in range(0,len(words),step)]
model=SentenceTransformer('all-MiniLM-L6-v2'); chunks=chunk(POLICY); vec=model.encode(chunks,convert_to_numpy=True).astype('float32'); index=faiss.IndexFlatL2(vec.shape[1]); index.add(vec)
def retrieve(query,k=3):
    k=min(k,index.ntotal); q=model.encode([query],convert_to_numpy=True).astype('float32'); d,ids=index.search(q,k); return [chunks[i] for i in ids[0]]
def build_rag_prompt(query,retrieved_chunks):
    context='\n'.join(f'{i}. {c}' for i,c in enumerate(retrieved_chunks,1)); return f'You are a policy assistant.\nRetrieved context:\n{context}\nUser question: {query}\nAnswer only from the context. If absent, say I don\'t know.'
if __name__=='__main__':
    q='What is the refund policy for missing items?'; r=retrieve(q); print('Chunk count:',len(chunks)); print('Retrieved:',r); print(build_rag_prompt(q,r)); print('Simulated answer: Missing-item refunds may be available after verification and timely reporting.')
