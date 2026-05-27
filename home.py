import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import seaborn as sns
import plotly.express as px

st.title("Welcome to the Sales Dashboard")
st.write("This dashboard provides insights into sales performance, customer behavior, and product trends. Explore the various sections to gain a deeper understanding of your sales data and make informed business decisions.")

## read file
df = pd.read_csv(r"D:\D_Drive\vamsi vs code\EDUKRON_FILES\PYTHON_FILES\project\sales_dashbord\data\Superstore sales dataset.csv")
st.write("Here is a preview of the sales dataset:")
st.dataframe(df.head())
shape = df.shape
st.write(f"The dataset contains {shape[0]} rows and {shape[1]} columns.")
Total_Sales = df['Sales'].sum()