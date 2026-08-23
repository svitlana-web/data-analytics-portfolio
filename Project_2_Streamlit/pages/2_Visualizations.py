import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Visualizations", page_icon="📊", layout="wide")
sns.set_theme(style="whitegrid")

st.title("📊 Data Visualizations & Insights")

if "df" not in st.session_state:
    st.warning("Please upload a dataset on the main page first.")
    st.stop()

df = st.session_state.df

# Core 4 charts dashboard
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('E-Commerce Business Analytics Overview', fontsize=18, fontweight='bold', y=0.98)

# 1. Bar Chart
if 'category' in df.columns and 'revenue' in df.columns:
    cat_rev = df.groupby('category')['revenue'].sum().reset_index().sort_values(by='revenue', ascending=False)
    ax1 = sns.barplot(data=cat_rev, x='category', y='revenue', ax=axes[0, 0], palette='Blues_r')
    axes[0, 0].set_title('1. Total Revenue by Category', fontsize=13, fontweight='bold', pad=10)
    for p in ax1.patches:
        height = p.get_height()
        ax1.annotate(f'${height:,.0f}', (p.get_x() + p.get_width() / 2., height),
                     ha='center', va='bottom', fontsize=9, xytext=(0, 3), textcoords='offset points')

# 2. Line Plot
if 'year_month' in df.columns and 'revenue' in df.columns:
    monthly_df = df.groupby('year_month')['revenue'].sum().reset_index()
    monthly_df['year_month_str'] = monthly_df['year_month'].astype(str)
    sns.lineplot(data=monthly_df, x='year_month_str', y='revenue', marker='o', color='#1f77b4', linewidth=2.5, markersize=8, ax=axes[0, 1])
    axes[0, 1].set_title('2. Monthly Revenue Dynamics (2025)', fontsize=13, fontweight='bold', pad=10)
    axes[0, 1].tick_params(axis='x', rotation=45)

# 3. Histogram
if 'revenue' in df.columns:
    sns.histplot(df['revenue'], kde=True, ax=axes[1, 0], color='#2ca02c', bins=20)
    axes[1, 0].axvline(df['revenue'].median(), color='red', linestyle='--', label=f"Median: ${df['revenue'].median():,.2f}")
    axes[1, 0].axvline(df['revenue'].mean(), color='orange', linestyle='-', label=f"Mean: ${df['revenue'].mean():,.2f}")
    axes[1, 0].set_title('3. Order Revenue Distribution', fontsize=13, fontweight='bold', pad=10)
    axes[1, 0].legend()

# 4. Pie Chart
if 'payment_method' in df.columns:
    payment_counts = df['payment_method'].value_counts()
    colors = sns.color_palette('pastel')[0:len(payment_counts)]
    axes[1, 1].pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=140, colors=colors, textprops={'fontsize': 10})
    axes[1, 1].set_title('4. Share of Payment Methods', fontsize=13, fontweight='bold', pad=10)

plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

# 5. Top 10 Cities
st.subheader("5. Top 10 Cities by Revenue")
if 'city' in df.columns and 'revenue' in df.columns:
    fig_city, ax5 = plt.subplots(figsize=(12, 6))
    city_rev = df.groupby('city')['revenue'].sum().reset_index().sort_values(by='revenue', ascending=False).head(10)
    
    sns.barplot(data=city_rev, y='city', x='revenue', hue='city', palette='viridis', legend=False, ax=ax5)
    ax5.set_title('5. Top 10 Cities by Revenue', fontsize=14, fontweight='bold', pad=15)
    ax5.set_xlabel('Revenue ($)', fontsize=12)
    ax5.set_ylabel('City', fontsize=12)

    max_val = city_rev['revenue'].max()
    ax5.set_xlim(0, max_val * 1.15)

    for p in ax5.patches:
        width = p.get_width()
        if width > 0:
            ax5.annotate(f'${width:,.0f}', (width, p.get_y() + p.get_height() / 2.),
                         ha='left', va='center', fontsize=10, xytext=(5, 0),
                         textcoords='offset points')

    plt.tight_layout()
    st.pyplot(fig_city)