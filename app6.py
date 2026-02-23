import streamlit as st 

st.title("Welcome to basic streamliy app")

name1 = st.text_input("Enter ur first name:")
name2 = st.text_input("Enter ur last name:")
email = st.text_input("Enter ur email id:")
gender = st.radio("Select ur gender",['Male','Female','Other'])
phn = st.number_input("Enter ur phone number",step =1 )
city = st.selectbox("Select ur city", ["Delhi","Mumbai","Nashik","Pune"])

if st.button("Submit"):
    st.write("First name:",name1)
    st.write("Last name:",name2)
    st.write("Email",email)
    st.write("Gender:",gender)
    st.write("Phone number:",phn)
    st.write("City:",city)