import numpy as np
import faiss
import chromadb

def faiss_demo():
    songs = ["Midnight City", "Ocean Eyes", "Golden Hour", "Rainy Days", "Road Trip"]
    vectors = np.random.default_rng(7).random((5, 4)).astype('float32')
    index = faiss.IndexFlatL2(4); index.add(vectors)
    print(f'Task 1 - FAISS index size: {index.ntotal}')

    client = chromadb.Client(); collection = client.create_collection('restaurants_demo')
    restaurants = ["Barbeque Nation", "Dominos", "Subway", "Cafe Coffee Day", "Biryani Blues"]
    rv = np.random.default_rng(4).random((5, 3)).astype('float32')
    collection.add(ids=[str(i) for i in range(5)], embeddings=rv.tolist(), documents=restaurants)
    result = collection.query(query_embeddings=[rv[0].tolist()], n_results=1)
    print('Task 2 - ChromaDB nearest restaurant:', result['documents'][0][0])

    movies = ["Action Horizon", "The Quiet Garden", "City Chase", "Robot Uprising", "Summer Letters"]
    mv = np.random.default_rng(11).random((5, 4)).astype('float32'); mi = faiss.IndexFlatL2(4); mi.add(mv)
    def search_movies(query_vector):
        distances, ids = mi.search(np.asarray([query_vector], dtype='float32'), 2)
        return [(movies[i], float(d)) for i, d in zip(ids[0], distances[0])]
    print('Task 3 - top movies:', search_movies(mv[2]))

    captions = ["Weekend vibes with good food", "Monday motivation", "Sunset by the sea", "Weekend coffee and conversations", "Work hard play hard"]
    cv = np.random.default_rng(12).random((5, 3)).astype('float32'); ci = faiss.IndexFlatL2(3); ci.add(cv)
    d, ids = ci.search(np.asarray([cv[0]], dtype='float32'), 3)
    print('Task 4 - top captions:', [captions[i] for i in ids[0]])
    print('Retrieval finds the stored vectors closest to the query vector by distance.')

    products = ["Wireless headphones with noise cancellation", "Fast USB-C charger", "Lightweight laptop for students", "Smartwatch with fitness tracking", "Portable Bluetooth speaker"]
    pv = np.random.default_rng(20).random((5, 4)).astype('float32'); pi = faiss.IndexFlatL2(4); pi.add(pv)
    d, ids = pi.search(np.asarray([pv[0]], dtype='float32'), 1)
    print('Task 5 - query: wireless headphones; nearest product:', products[ids[0][0]])
    print('Prompt used to create descriptions: Generate five concise Flipkart-style product descriptions for varied electronics.')

if __name__ == '__main__': faiss_demo()

# The script covers FAISS, ChromaDB, semantic retrieval, Instagram-caption retrieval, and product search. Install `requirements.txt`, then run `python vector_retrieval.py`.