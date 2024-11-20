import pandas as pd
import streamlit as st
import plotly.express as px

# Load dataset
data = pd.read_csv('train.csv')

# Streamlit App
st.title("Superstore Sales Dashboard")

# Filter by region
region = st.sidebar.selectbox("Select Region", data["Region"].unique())

# Filter data
filtered_data = data[data["Region"] == region]

# Visualization 1: Sales by Category
fig1 = px.bar(filtered_data, x="Category", y="Sales", title="Sales by Category")
st.plotly_chart(fig1)

# Visualization 2: Sales Over Time
# Specify dayfirst=True to handle European-style dates
filtered_data["Order Date"] = pd.to_datetime(filtered_data["Order Date"], dayfirst=True)

# Group data by month and sum sales
sales_over_time = filtered_data.groupby(filtered_data["Order Date"].dt.to_period("M"))["Sales"].sum().reset_index()
sales_over_time["Order Date"] = sales_over_time["Order Date"].astype(str)  # Convert Period to string for plotting
fig2 = px.line(sales_over_time, x="Order Date", y="Sales", title="Monthly Sales Trend")
st.plotly_chart(fig2)

st.write("Data Snapshot:")
st.write(filtered_data.head())
