import streamlit as st

# Function to perform calculation
def calculate(num1, num2, operation):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2
    else:
        return "Invalid operation"

# Streamlit app layout
st.title("Simple Streamlit Calculator")

# User input
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform calculation and display result
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.write(f"Result: {result}")
