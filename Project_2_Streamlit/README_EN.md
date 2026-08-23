# E-Commerce Data Analytics & Interactive Streamlit Dashboard

A data analysis project and interactive dashboard designed to explore e-commerce sales performance, revenue distribution, payment methods, and customer order metrics.

## 🔗 Links
* **Streamlit App:** [Streamlit App Link will be placed here]
* **Jupyter Notebook EDA:** `notebooks/01_eda_and_analysis.ipynb`

## 🛠 Tech Stack
* **Python**: `pandas`, `numpy` (data preprocessing & manipulation)
* **Visualization**: `matplotlib`, `seaborn`, `plotly`
* **Dashboard Framework**: `streamlit`

## 📁 Project Structure
* `data/` — source and processed dataset.
* `notebooks/` — Exploratory Data Analysis (EDA) & initial visualizations.
* `pages/` — pages for multi-page Streamlit layout (detailed views & charts).
* `app.py` — main page of the Streamlit interactive web dashboard.
* `requirements.txt` — project dependency list.

## 🚀 Quick Start
1. Clone the repository: `git clone <URL>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run Streamlit: `streamlit run app.py`


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📊 Project Progress & Key Findings


### 1. Data Preprocessing

* **Data Cleaning:**

  * Stripped non-numeric characters and corrected data types for `quantity`, `price_per_unit`, and `revenue`.
  * Parsed `order_date` into standard `datetime` format and extracted the `year_month` period.
  * Imputed missing values in categorical fields (`city`, `payment_method`) as `Unknown`, recalculated missing `revenue` entries considering discounts. The final dataset consists of 293 cleaned rows.


### 2. Exploratory Data Analysis (EDA)

* **Key Insights (Pandas Analysis):**
  * **Most Popular Product:** Keyboard (110 units sold) and Smartphone (107 units sold).
  * **Top Category by Revenue:** Electronics ($398,911, representing over 45% of total revenue).
  * **Peak Sales Month:** August 2025 ($97,212).
  * **Average Order Value (AOV):** $3,029.67 (Median: $2,589.00).
  * **Top Customer by Orders:** Daniel (41 orders).


### 3. Data Visualization (Matplotlib & Seaborn)

A series of 5 interactive and annotated charts was developed to analyze core e-commerce business performance metrics:

* **Revenue by Category (Annotated Bar Chart):** 
  Highlights *Electronics* as the primary revenue generator (**$398,911**), almost doubling the second-largest category, *Fashion* (**$203,905**).
* **Monthly Revenue Dynamics (Line Plot):** 
  Reveals strong seasonal growth during the summer months (**May–August 2025**), reaching a year-high peak in August at **$97,212**.
* **Order Revenue Distribution (Histogram + KDE):** 
  Shows a right-skewed distribution where low to mid-tier orders (under $2,500) dominate. Premium purchases push the average order value (**$3,029.67**) well above the median (**$2,589.00**).
* **Payment Methods Share (Pie Chart):** 
  Illustrates customer preferences, showing a high adoption rate for **PayPal (37.9%)** and **Credit Cards (32.8%)**, followed by **Cash (28.0%)**.
* **Top 10 Cities by Revenue (Horizontal Bar Chart):** 
  Provides geographic breakdown of sales, identifying **Paris ($150,454)** as the top-performing market alongside Yerevan and Madrid for localized targeted strategy.



### 4. Streamlit Web Application

A modular multi-page analytical web service was built using Streamlit to interactively explore and visualize e-commerce performance metrics:

* **Data Upload & Preprocessing (`Data Overview`):** 
  Features an intuitive CSV uploader with automated data cleaning, type conversion, and raw data preview.
* **Analytical Indicators & KPIs (`Analytics & Stats`):** 
  Displays high-level business metrics (Total Revenue, Average/Median Order Value, Max Order Value) along with grouped tables for categories, payment methods, monthly dynamics, and top-performing cities.
* **Interactive Dashboard (`Visualizations`):** 
  Renders all 5 Matplotlib/Seaborn visualizations, providing clear visual insights into sales distribution, seasonality, and regional performance.
* **State Management (`st.session_state`):** 
  Ensures seamless data persistence across all subpages after a single file upload.

🚀 **Live Streamlit App:** [Link will be added after deployment]
