import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

st.title("Q and A Chat Bot")

# Use a try-except block to catch errors
try:
    btn_create_kb = st.button("Create Knowledgebase")
    if btn_create_kb:
        create_vector_db()

    question = st.text_input("Question: ")

    # Add a submit button
    btn_submit = st.button("Submit")

    if btn_submit and question:
        chain = get_qa_chain()
        response = chain(question)

        st.header("Answer")
        st.write(response["result"])

except Exception as e:
    st.error(f"An error occurred: {e}")
