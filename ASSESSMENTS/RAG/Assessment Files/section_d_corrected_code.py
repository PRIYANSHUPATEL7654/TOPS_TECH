import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
text=open('section_d_refund_policy.txt',encoding='utf8').read()
chunks=[text[i:i+200].strip() for i in range(0,len(text),200) if text[i:i+200].strip()]
model=SentenceTransformer('all-MiniLM-L6-v2'); embeddings=model.encode(chunks,convert_to_numpy=True).astype('float32')
index=faiss.IndexFlatL2(embeddings.shape[1]); index.add(embeddings)
while True:
    question=input('Question (type quit to exit): ').strip()
    if question.lower()=='quit': print('Exited cleanly.'); break
    if not question: print('Please enter a question.'); continue
    k=min(2,index.ntotal); q=model.encode([question],convert_to_numpy=True).astype('float32'); distances,ids=index.search(q,k)
    context='\n'.join(chunks[i] for i in ids[0])
    prompt=f"Role: food-delivery policy assistant.\nContext:\n{context}\nQuestion: {question}\nAnswer only from the provided context. If the answer is not present, say I do not know."
    print('Retrieved context:',context); print('Assembled prompt:',prompt); print('Simulated answer: Review the retrieved policy context.')
