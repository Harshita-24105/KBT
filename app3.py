import streamlit as st 

st.title("Basic Calculator")

num1 = st.number_input("Enter ur 1st num:",step = 1)
num2 = st.number_input("Enter ur 2nd num:",step = 1)

 
operation = st.selectbox("Choose Opeation",['add','sub','mul','div'])

if st.button("Calculate"):
    if operation=='add':
        st.write(num1 + num2)

    elif operation=='sub':
        st.write(num1-num2)

    elif operation=='mul':
        st.write(num1*num2)

    elif operation=='div':
        if num2 !=0:
            st.write(num1/num2)
        else:
            st.write("Error!!!!")