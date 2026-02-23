import streamlit as st 

st.title("Simple input app")

name = st.text_input("Enter ur name:")
if st.button("submit"):
    st.write("Hello,",name)