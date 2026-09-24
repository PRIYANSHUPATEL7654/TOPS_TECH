"""Streamlit vector-search chatbot: reviews in Chroma + local food-facts file."""
from pathlib import Path
import streamlit as st
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
REVIEWS=["The paneer pizza was cheesy, fresh, and delicious.","Best spicy biryani I have ordered this month.","The dosa was crisp and the coconut chutney tasted fresh.","Tasty noodles with generous vegetables and quick delivery.","The chocolate brownie was warm, rich, and soft."]
st.set_page_config(page_title="QuickBite RAG",page_icon="🍲")
st.title("🍲 Food Q&A — Retrieval Demo")
@st.cache_resource
def load_db():
    emb=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db=Chroma(collection_name="session5_reviews",embedding_function=emb,persist_directory=str(Path(__file__).resolve().parents[1]/"chroma_db"))
    if db._collection.count()==0:db.add_texts(REVIEWS)
    return db,emb
def facts():return (Path(__file__).resolve().parents[1]/"quickbite/food_facts.txt").read_text(encoding="utf-8").splitlines()
q=st.chat_input("Ask about food recommendations or facts")
if q:
    with st.chat_message("user"):st.write(q)
    try:
        db,emb=load_db(); review=db.similarity_search(q,k=1)[0].page_content
        fact_list=facts(); qvec=emb.embed_query(q); fvecs=emb.embed_documents(fact_list)
        import numpy as np
        scores=[float(np.dot(qvec,v)/(np.linalg.norm(qvec)*np.linalg.norm(v))) for v in fvecs]
        fact=fact_list[int(np.argmax(scores))]
        answer=f"Most relevant customer review: {review}\n\nRelated food fact: {fact}"
    except Exception as exc:answer=f"Retrieval setup issue: {exc}. Install requirements and retry."
    with st.chat_message("assistant"):st.write(answer)
st.caption("RAG retrieves relevant evidence before responding; it can still miss facts if the source or retrieval is poor.")
