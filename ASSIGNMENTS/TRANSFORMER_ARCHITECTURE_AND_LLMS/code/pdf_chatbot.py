"""Session 6 Task 1 - PDF Chatbot: upload a PDF, extract text with PyPDF2, show it in the browser.
Run with:  pip install streamlit PyPDF2   then   streamlit run pdf_chatbot.py"""
import streamlit as st
from PyPDF2 import PdfReader


def extract_text(file) -> str:
    reader = PdfReader(file)
    return "\n\n".join("--- Page %d ---\n%s" % (i, (p.extract_text() or "").strip()) for i, p in enumerate(reader.pages, 1))


st.title("📄 PDF Chatbot")
uploaded = st.file_uploader("Upload a PDF (college timetable, IRCTC ticket, ...)", type="pdf")
if uploaded is not None:
    text = extract_text(uploaded)
    st.subheader("Extracted text")
    st.text_area("Text from your PDF", text, height=400)
