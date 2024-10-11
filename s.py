import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Input text box
user_input = st.text_input("Enter some text:")

# Display the input text
if user_input:
    st.write("You entered:", user_input)

# Add a slider
number = st.slider("Select a number:", 0, 100, 50)

# Display the selected number
st.write("You selected:", number)

# Button to clear the input
if st.button("Clear"):
    st.experimental_rerun()  # Refreshes the app to clear input
