import streamlit as st
st.header('Find the :rainbow[maximum] of :rainbow[three] numbers', divider='rainbow')
num1 = st.number_input(label = "Enter :rainbow[1st] number", value = None, placeholder = "1st number...")
num2 = st.number_input(label = "Enter :rainbow[2nd] number", value = None, placeholder = "2nd number...")
num3 = st.number_input(label = "Enter :rainbow[3rd] number", value = None, placeholder = "3rd number...")
if (num1 != None and num2 != None and num3 != None):
    st.write(f":rainbow[Maximum] value among the three numbers:    :rainbow[{str(max(num1, num2, num3))}]")
