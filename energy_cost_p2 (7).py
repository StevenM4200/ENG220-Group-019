# -*- coding: utf-8 -*-
"""Energy Cost p2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-1BGnnuqc-1f0ZDyERhxIrFx_Z36VJ1X
"""

# Import necessary libraries
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit app
st.title('Manually Plot Points for Functions')

# Manually define the years and function values
years = np.array([2017, 2018, 2019, 2020, 2021, 2022])

# Manually defined values for each function
f1_values = np.array([24.13, 27.04, 25.57, 22.34, 28.86, 36.02])  # f1 values
f2_values = np.array([26.5, 35.3, 54.8, 49.5, 52.1, 32.9])        # f2 values
f3_values = np.array([1.1, 0.9, 1.6, 1.3, 1.5, 3.0])              # f3 values
f4_values = np.array([3.0, 4.0, 2.0, 2.0, 2.0, 15.0])             # f4 values
f5_values = np.array([0.7, 1.3, 1.8, 2.5, 4.1, 6.2])              # f5 values

# Plotting the graph using matplotlib
plt.figure(figsize=(10, 6))

# Plot each function
plt.plot(years, f1_values, label='ARICD', marker='o', linewidth=2)
plt.plot(years, f2_values, label='ARTCD', marker='o', linewidth=2)
plt.plot(years, f3_values, label='ARTXD', marker='o', linewidth=2)
plt.plot(years, f4_values, label='AVACD', marker='o', linewidth=2)
plt.plot(years, f5_values, label='AVTCD', marker='o', linewidth=2)

# Title and labels
plt.title('Price Percent Increase over Years')
plt.xlabel('Year')
plt.ylabel('Price Percent Increase')

# Show legend
plt.legend()

# Show grid
plt.grid(True)

# Display the plot in Streamlit
st.pyplot(plt)