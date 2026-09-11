from pathlib import Path
import numpy as np
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer

def extract_text(pdf_path):
    return '\n'.join(page.extract_text() or '' for page in PdfReader(pdf_path).pages)

def chunks(text, size=500): return [text[i:i+size] for i in range(0, len(text), size)]

def main():
    text = extract_text('sample_resume.pdf')
    print('Task 1 - extracted PDF text:\n', text)
    pieces = chunks(text)
    print(f'\nTask 2 - number of 500-character chunks: {len(pieces)}')
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    vectors = model.encode(pieces, convert_to_numpy=True)
    question = 'Who messaged the most?'
    q = model.encode([question], convert_to_numpy=True)[0]
    scores = vectors @ q / (np.linalg.norm(vectors, axis=1) * np.linalg.norm(q))
    best = int(np.argmax(scores))
    print(f'Task 3 - embeddings stored: {len(vectors)}')
    print(f'Task 4 - best chunk score {scores[best]:.4f}: {pieces[best]}')
    print('Task 5 - deployment ideas: restaurant policy assistant, IRCTC booking-help assistant, and movie venue FAQ assistant.\n1. Restaurant policy assistant\nUsers could upload or access restaurant menus, refund policies, delivery rules, and cancellation policies. The chatbot would quickly answer questions about ingredients, prices, delivery charges, refunds, and order cancellations.\n2. IRCTC booking-help assistant\nUsers could ask questions from railway rules, ticket-booking instructions, cancellation policies, baggage rules, and concession guidelines. This would help passengers find accurate information without reading lengthy documents.\n3. Movie venue FAQ assistant\nUsers could ask questions about event rules, theatre policies, ticket cancellation, age restrictions, venue facilities, and entry requirements. This would make it easier to understand event details before booking or attending.')

if __name__ == '__main__': main()

# Run `python pdf_chatbot.py` after installing `requirements.txt`. `sample_resume.pdf` is included as a test input. The script also demonstrates chunking, embeddings, similarity search, and deployment ideas.
