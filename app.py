import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('Basic Streamlit App')

# Description
st.write("""
This is a simple Streamlit app to demonstrate basic functionalities.
You can use this template to build more complex machine learning applications.
""")

# Sidebar for user input
st.sidebar.header('User Input Parameters')

def user_input_features():
    param1 = st.sidebar.slider('Parameter 1', 0.0, 10.0, 5.0)
    param2 = st.sidebar.slider('Parameter 2', 0.0, 10.0, 5.0)
    param3 = st.sidebar.slider('Parameter 3', 0.0, 10.0, 5.0)
    data = {'Parameter 1': param1,
            'Parameter 2': param2,
            'Parameter 3': param3}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Display user input parameters
st.subheader('User Input Parameters')
st.write(df)

# Generate random data for demonstration
data = np.random.randn(100, 3)
df_data = pd.DataFrame(data, columns=['Feature 1', 'Feature 2', 'Feature 3'])

# Display the data
st.subheader('Random Data')
st.write(df_data)

# Plot the data
st.subheader('Data Visualization')
st.line_chart(df_data)
