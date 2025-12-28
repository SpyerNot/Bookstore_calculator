import streamlit as st
st.title("Bookstore calculator")
st.caption("Used to calculate all the stationaries without using an actual calculator")
option = st.selectbox("What level is the buyer studying?", ("S1","S2","S3","S4","S5"),)
s1 = s3 = 138
s2 = 134.6
s4e = 119.3
s4na = 115.5
s4nt = 118.7
if option == "S1" or option == "S3":
  st.write("The total cost of the stationaries is $138")
  remove_cost = st.number_input("Enter the cost you want to remove: ")
  s1 = s1 - remove_cost 
