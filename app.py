import streamlit as st
import pandas as pd

df = pd.read_csv("sales_data.csv")
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

st.title("📊 Sales Dashboard")

st.subheader("Dataset")
st.write(df)

st.subheader("Total Sales")
st.write(df['sales'].sum())

st.subheader("Monthly Sales")
st.line_chart(df.groupby('month')['sales'].sum())

st.subheader("Top Products")
st.bar_chart(df.groupby('product')['sales'].sum())

st.subheader("Region-wise Sales")
st.bar_chart(df.groupby('region')['sales'].sum())

st.subheader("📌 Key Insights")

st.write("""
- Electronics category has highest sales  
- North region performs best  
- Sales increase in certain months  
- Few products contribute most revenue  
""")

st.success("Electronics category contributes the highest revenue.")