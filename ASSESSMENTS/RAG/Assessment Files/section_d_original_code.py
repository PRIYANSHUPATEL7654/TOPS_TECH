import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
text=open('section_d_refund_policy.txt').read()
chunks=[text[i:i+200] for i in range(0,len(text),200)]
model=SentenceTransformer('all-MiniLM-L6-v2')
embeddings=model.encode(chunks).astype('float32')
index=faiss.IndexFlatL2(embeddings.shape[1]); index.add(embeddings)
while True:
    question=input('Question: ')
    if question=='quit': break
    q=model.encode([question]).astype('float32'); distances,ids=index.search(q,2)
    context='\n'.join(chunks[i] for i in ids[0])
    print('Context:',context)
    print('Prompt: Answer the question using this context: '+context+' Question: '+question)
    print('Simulated answer: Review the retrieved policy context.')
