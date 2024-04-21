import streamlit as st
num1 = st.number_input(label = "Enter 1st number", value = None, placeholder = "1st number...")
num2 = st.number_input(label = "Enter 2nd number", value = None, placeholder = "2nd number...")
num3 = st.number_input(label = "Enter 3rd number", value = None, placeholder = "3rd number...")
st.write("Max value among the three numbers: ", max(num1, num2, num3))
