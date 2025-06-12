import streamlit as st
from ask_question import ask_question
import pandas as pd

st.set_page_config(page_title="Wasserstoff Theme Chatbot", layout="wide")
st.title("📄 Document Research & Theme Identification Chatbot")

query = st.text_input(" Ask a question about your documents")

if query:
    with st.spinner("Analyzing documents and generating answer..."):
        answer, docs, metas = ask_question(query)

    st.markdown("### Synthesized Answer")
    st.write(answer)

    # Creating citation table
    st.markdown("### Relevant Snippets With Citations")
    df = pd.DataFrame([
        {
            "Document": meta["source"],
            "Chunk": meta["chunk"],
            "Snippet": doc[:300] + "..."
        } for doc, meta in zip(docs, metas)
    ])
    st.dataframe(df)