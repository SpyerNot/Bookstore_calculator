import streamlit as st
st.title("Bookstore calculator")
st.caption("Used to calculate all the stationaries without using an actual calculator")
option = st.selectbox("What level is the buyer studying?", ("S1","S2","S3","S4","S5"),)
s1 = 138
s2 = 134.6
s4e = 119.3
s4na = 115.5
s4nt = 118.7
if option == "S1" or option == "S3":
  st.write("The total cost of the stationaries is $138")
  remove = st.number_input("Enter the cost that you want to deduct off $138: ", min_value = -1)
  while True:
    if remove == 0:
      break
      st.write(s1)
    else:
      s1 = s1 - remove
      remove = st.number_input("Enter the cost that you want to deduct off: ", min_value = -1)
