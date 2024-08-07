import streamlit as st

# Title of the app
st.title('Simple Calculator')

# Input fields for numbers
num1 = st.number_input('Enter the first number:')
num2 = st.number_input('Enter the second number:')

# Dropdown for selecting operation
operation = st.selectbox('Select operation', ['Addition', 'Subtraction', 'Multiplication', 'Division'])

# Perform calculation based on operation selected
if operation == 'Addition':
    result = num1 + num2
elif operation == 'Subtraction':
    result = num1 - num2
elif operation == 'Multiplication':
    result = num1 * num2
elif operation == 'Division':
    if num2 != 0:
        result = num1 / num2
    else:
        result = 'Error: Division by zero'
else:
    result = ''

# Display result
st.write('Result:', result)
