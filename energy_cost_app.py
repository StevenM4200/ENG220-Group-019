# -*- coding: utf-8 -*-
"""Energy Cost App

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eK2Bup0c4SoesAKXv2jXTyPE2y-n4Xwq
"""

# Import necessary libraries
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

# Function to generate random coefficients
def generate_random_function():
    # Randomly generate coefficients for a quadratic, cubic or exponential function
    a = random.uniform(-10, 10)
    b = random.uniform(-10, 10)
    c = random.uniform(-10, 10)
    return lambda x: a * np.sin(b * x) + c * np.cos(a * x)

# Streamlit app
st.title('Random Mathematical Functions Plot')

# Generate year range
years = np.linspace(2000, 2024, 25)  # From year 2000 to 2024

# Generate 5 random functions
functions = [generate_random_function() for _ in range(5)]

# Plot the functions
plt.figure(figsize=(10, 6))

for i, func in enumerate(functions, start=1):
    plt.plot(years, func(years), label=f'f{i}', linewidth=2)

# Labeling the graph
plt.title('Price vs Year')
plt.xlabel('Year')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Display the plot in the notebook
st.pyplot(plt)