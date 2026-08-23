import streamlit as st
import pandas as pd

st.set_page_config(page_title="Analytics & Stats", page_icon="📈", layout="wide")

st.title("📈 Key Analytical Indicators")

if "df" not in st.session_state:
    st.warning("Please upload a dataset on the main page first.")
    st.stop()

df = st.session_state.df

# Core KPIs
total_revenue = df['revenue'].sum() if 'revenue' in df.columns else 0
total_orders = df.shape[0]
avg_order_value = df['revenue'].mean() if 'revenue' in df.columns else 0
median_order_value = df['revenue'].median() if 'revenue' in df.columns else 0
std_order_value = df['revenue'].std() if 'revenue' in df.columns else 0
max_order_value = df['revenue'].max() if 'revenue' in df.columns else 0

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Avg Order Value", f"${avg_order_value:,.2f}")
col4.metric("Median Order Value", f"${median_order_value:,.2f}")
col5.metric("Max Order Value", f"${max_order_value:,.2f}")

st.markdown("---")

# Row 1: Category Breakdown & Payment Methods
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("1. Revenue by Category")
    if 'category' in df.columns and 'revenue' in df.columns:
        cat_stats = df.groupby('category')['revenue'].agg(['sum', 'mean', 'count']).reset_index()
        cat_stats.columns = ['Category', 'Total Revenue ($)', 'Average Purchase ($)', 'Order Count']
        cat_stats['Total Revenue ($)'] = cat_stats['Total Revenue ($)'].apply(lambda x: f"${x:,.2f}")
        cat_stats['Average Purchase ($)'] = cat_stats['Average Purchase ($)'].apply(lambda x: f"${x:,.2f}")
        st.dataframe(cat_stats.sort_values(by='Order Count', ascending=False), use_container_width=True)

with col_right:
    st.subheader("2. Payment Methods Share")
    if 'payment_method' in df.columns:
        pay_stats = df['payment_method'].value_counts().reset_index()
        pay_stats.columns = ['Payment Method', 'Count']
        pay_stats['Share (%)'] = (pay_stats['Count'] / pay_stats['Count'].sum() * 100).round(1)
        st.dataframe(pay_stats, use_container_width=True)

st.markdown("---")

# Row 2: Monthly Dynamics & Top Cities
col_m1, col_m2 = st.columns(2)

with col_m1:
    st.subheader("3. Monthly Sales Dynamics")
    if 'year_month' in df.columns and 'revenue' in df.columns:
        monthly_stats = df.groupby('year_month')['revenue'].agg(['sum', 'count']).reset_index()
        monthly_stats.columns = ['Year-Month', 'Total Revenue ($)', 'Orders']
        monthly_stats['Total Revenue ($)'] = monthly_stats['Total Revenue ($)'].apply(lambda x: f"${x:,.2f}")
        st.dataframe(monthly_stats, use_container_width=True)

with col_m2:
    st.subheader("4. Top 10 Cities by Revenue")
    if 'city' in df.columns and 'revenue' in df.columns:
        city_stats = df.groupby('city')['revenue'].agg(['sum', 'count']).reset_index().sort_values(by='sum', ascending=False).head(10)
        city_stats.columns = ['City', 'Total Revenue ($)', 'Orders']
        city_stats['Total Revenue ($)'] = city_stats['Total Revenue ($)'].apply(lambda x: f"${x:,.2f}")
        st.dataframe(city_stats, use_container_width=True)