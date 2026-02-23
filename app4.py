import streamlit as st 

st.title("My Chatbot")

ques = st.text_input("Ask me anything")

if st.button("send"):
    st.write("You asked",ques)
    st.write("chatbot is on the process i will reply soon")