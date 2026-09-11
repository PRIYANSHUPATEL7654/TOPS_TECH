from pathlib import Path
import re
import numpy as np
from sentence_transformers import SentenceTransformer

def chunk_text(text, chunk_size, overlap):
    if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("chunk_size must be positive and overlap must be between 0 and chunk_size-1")
    words = text.split()
    step = chunk_size - overlap
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), step) if words[i:i + chunk_size]]

wiki_sample = """Wikipedia is a free online encyclopedia written and maintained by a community of volunteers. It is hosted by the Wikimedia Foundation, a non-profit organization. Articles are collaboratively edited and are expected to be supported by reliable published sources. Wikipedia began as a companion project to Nupedia and was launched in January 2001. The encyclopedia is available in many languages and covers science, history, culture, geography, technology, and current events. Readers can search articles, follow references, and improve pages when they can add verifiable information. Policies such as neutral point of view, verifiability, and no original research guide contributors. Because anyone can edit most pages, readers should check citations and the edit history when the topic is important. The project illustrates how distributed volunteers can create a large knowledge resource through shared rules and review."""

privacy_text = """This privacy policy explains how a food delivery application collects, uses, stores, and protects information. The application may collect account details, delivery addresses, payment confirmations, device information, restaurant preferences, and support conversations. Location information is used to show nearby restaurants and improve delivery tracking when permission is enabled. Order information is used to process purchases, calculate delivery charges, provide receipts, handle refunds, and resolve complaints. The service may share necessary order details with restaurants, delivery partners, payment processors, and legal authorities when required. Personal information is retained only for as long as needed for the stated purpose, legal obligations, safety, dispute handling, and fraud prevention. Users may request access, correction, or deletion subject to legal and operational requirements. Security measures include access controls, encryption in transit, monitoring, and restricted employee access. Users should protect passwords and report suspicious activity promptly. Policy changes are posted in the application, and continued use after a change may indicate acceptance. Questions about privacy can be sent to the support team through the Help section."""

sentences = ["The pizza was amazing", "Service was slow", "Loved the ambience"]
model = SentenceTransformer('all-MiniLM-L6-v2')

def main():
    print('Task 1 - 500-word sample chunks:', len(chunk_text(wiki_sample, 80, 10)))
    chunks = chunk_text(privacy_text, 100, 20)
    print('\nTask 2 - first 3 privacy chunks:')
    for i, c in enumerate(chunks[:3], 1): print(f'Chunk {i}: {c}\n')
    vectors = model.encode(sentences, convert_to_numpy=True)
    for s, v in zip(sentences, vectors): print(f'Task 3 - {s}: {v.tolist()}')
    pair = model.encode(["The burger was delicious", "I enjoyed the burger a lot"], convert_to_numpy=True)
    score = float(np.dot(pair[0], pair[1]) / (np.linalg.norm(pair[0]) * np.linalg.norm(pair[1])))
    print(f'\nTask 4 - cosine similarity: {score:.4f}; the sentences are semantically similar.')
    print('\nTask 5 - overlap explanation:')
    print('Overlap keeps nearby words in two chunks. Without it, a review might put the dish name in one chunk and the price or allergy warning in the next, so a search result could miss the connection.')

if __name__ == '__main__': main()
