import streamlit as st 

st.title("Welcome to basic streamliy app")

age = st.slider("Select ur age", 1 , 100)

city = st.selectbox("Select ur city", ["Delhi","Mumbai","Nashik","Pune"])

if st.button("Show the details"):
    st.write("Age:",age)
    st.write("City:",city)