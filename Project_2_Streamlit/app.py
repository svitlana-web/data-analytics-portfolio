import streamlit as st
import pandas as pd

# Define Navigation Structure (Best Practice for Streamlit)
overview_page = st.Page("app.py", title="Data Overview", icon="📂", default=True)
analytics_page = st.Page("pages/1_Analytics_and_Stats.py", title="Analytics & Stats", icon="📈")
visuals_page = st.Page("pages/2_Visualizations.py", title="Visualizations", icon="📊")

pg = st.navigation([overview_page, analytics_page, visuals_page])
st.set_page_config(page_title="E-Commerce Analytics Hub", page_icon="📊", layout="wide")

# Run selected navigation page code
if pg.title == "Data Overview":
    st.title("📂 E-Commerce Analytics Hub")
    st.subheader("Data Upload & Preprocessing")
    st.markdown("Upload your raw CSV dataset here to clean the data and activate insights across all pages.")

    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    @st.cache_data
    def load_and_clean_data(file):
        df = pd.read_csv(file)
        
        if 'revenue' in df.columns:
            df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
            df = df[df['revenue'] >= 0]
            
        if 'quantity' in df.columns:
            df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
            df = df[df['quantity'] > 0]
            
        if 'order_date' in df.columns:
            df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
            df['year_month'] = df['order_date'].dt.to_period('M')
            
        df = df.drop_duplicates()
        return df

    if uploaded_file is not None:
        st.session_state.df = load_and_clean_data(uploaded_file)

    if "df" in st.session_state:
        st.success("Dataset is active and ready for analysis!")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Rows (Records)", f"{st.session_state.df.shape[0]:,}")
        with col2:
            st.metric("Total Columns (Features)", st.session_state.df.shape[1])
            
        st.subheader("Dataset Preview (Top 10 Rows)")
        st.dataframe(st.session_state.df.head(10), use_container_width=True)
    else:
        st.info("Please upload a CSV file above to start the analysis.")
else:
    pg.run()