import streamlit as st
from ingest import load_pdf
from retriever import chunk_text, build_index, retrieve
from llm_clients import ask_llm

st.title("📄 Document Q&A (RAG-lite)")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    text = load_pdf(uploaded_file)
    chunks = chunk_text(text)
    index, _ = build_index(chunks)

    question = st.text_input("Ask a question about the document")

    if question:
        context = retrieve(question, index, chunks)

        prompt = f"""
Use ONLY the context below to answer.
If not found, say "I don't know".

Context:
{context}

Question:
{question}
"""

        with st.spinner("Searching document..."):
            answer = ask_llm(prompt)

        st.markdown("### Answer")
        st.write(answer)