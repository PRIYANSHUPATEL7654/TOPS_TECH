import numpy as np, faiss
from sentence_transformers import SentenceTransformer
FAQS = ['Delivery usually arrives within 30 to 45 minutes.', 'Orders can be cancelled before the restaurant accepts them.', 'Refunds are available for missing items after verification.', 'A customer may request an item substitution through support.', 'Contact support from the Help section for order problems.', 'Delivery fees depend on distance, demand, and restaurant location.']
model = SentenceTransformer('all-MiniLM-L6-v2'); embeddings = model.encode(FAQS, convert_to_numpy=True).astype('float32')
index = faiss.IndexFlatL2(embeddings.shape[1]); index.add(embeddings); print('Index size:', index.ntotal)
def search_faq(query, k=2):
    k = min(k, index.ntotal); q = model.encode([query], convert_to_numpy=True).astype('float32'); distances, ids = index.search(q, k)
    return [(FAQS[i], float(d)) for i, d in zip(ids[0], distances[0])]
if __name__ == '__main__':
    for q in ['How do I get money back?', 'Can I stop my order?']: print(q, search_faq(q))
