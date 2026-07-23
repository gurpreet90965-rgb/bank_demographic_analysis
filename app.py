import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("🏦 Bank Data Analysis Dashboard")

# Uploaded file
def load_data():
    df = pd.read_csv("Bank_Transaction_Fraud_Detection.csv")
    return df

# Sidebar
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Select Section",
    ["Data Overview","Statistics","Missing Values","Correlation Heatmap"]
)
st.header("Dataset Overview")
st.write(df.head())

st.subheader("Shape of Dataset")
st.write(df.shape)