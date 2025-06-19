import streamlit as st
import pandas as pd
import plotly.express as px
import io
from utils.data_loader import load_data
from utils.plotting import create_plot
from pandas.api.types import is_object_dtype, is_categorical_dtype, is_numeric_dtype


st.set_page_config(page_title="Data Dashboard", initial_sidebar_state="expanded", layout="wide")

st.title("📊 Interactive Data Dashboard")

# Sidebar file upload
uploaded_file = st.sidebar.file_uploader("Upload your data file", type=["csv", "xlsx"])

# Sample dataset as fallback
if uploaded_file:
    df = load_data(uploaded_file)
else:
    st.sidebar.info("Using sample dataset")
    df = pd.read_csv("assets/sample_dataset.csv")

# Show dataframe
st.subheader("Data Preview")
st.dataframe(df)

# Column filters
st.sidebar.header("Filters")
filters = {}

for col in df.columns:
    if is_object_dtype(df[col]) or is_categorical_dtype(df[col]):
        options = df[col].dropna().unique()
        selected = st.sidebar.multiselect(f"Filter {col}", options, default=options)
        filters[col] = selected
    elif is_numeric_dtype(df[col]):
        min_val = float(df[col].min())
        max_val = float(df[col].max())
        selected_range = st.sidebar.slider(f"Filter {col}", min_val, max_val, (min_val, max_val))
        filters[col] = selected_range

mask = pd.Series(True, index=df.index)
for col, condition in filters.items():
    if isinstance(condition, list):
        mask &= df[col].isin(condition)
    elif isinstance(condition, tuple) and len(condition) == 2:
        mask &= df[col].between(condition[0], condition[1])
filtered_df = df[mask]

# Display stats
st.subheader("Summary Statistics")
st.write(filtered_df.describe())

# Data Visualization
st.subheader("Data Visualization")

if filtered_df.empty:
    st.warning("No data available after applying filters.")
    st.stop()

chart_options = ["Bar Chart", "Line Chart", "Scatter Plot", "Pie Chart", "Histogram"]
chart_type = st.selectbox("Select chart type", chart_options, index=0)

if chart_type in ["Bar Chart", "Line Chart", "Scatter Plot"]:
    x_axis = st.selectbox("Select X-axis", filtered_df.columns, index=0)
    y_numeric_cols = filtered_df.select_dtypes(include="number").columns
    if y_numeric_cols.empty:
        st.warning("No numeric columns available for Y-axis.")
        st.stop()
    y_axis = st.selectbox("Select Y-axis", y_numeric_cols, index=0)
    fig = create_plot(chart_type, filtered_df, x_axis=x_axis, y_axis=y_axis)

elif chart_type == "Pie Chart":
    cat_cols = filtered_df.select_dtypes(include=["object", "category"]).columns
    num_cols = filtered_df.select_dtypes(include="number").columns
    if cat_cols.empty or num_cols.empty:
        st.warning("A pie chart requires at least one categorical and one numeric column.")
        st.stop()
    cat_column = st.selectbox("Select categorical column", cat_cols, index=0)
    num_column = st.selectbox("Select numeric column", num_cols, index=0)
    fig = create_plot(chart_type, filtered_df, cat_col=cat_column, num_col=num_column)

elif chart_type == "Histogram":
    hist_cols = filtered_df.select_dtypes(include="number").columns
    if hist_cols.empty:
        st.warning("No numeric columns available for histogram.")
        st.stop()
    hist_column = st.selectbox("Select numeric column", hist_cols, index=0)
    fig = create_plot(chart_type, filtered_df, num_col=hist_column)

st.plotly_chart(fig, use_container_width=True)

# Download filtered data
st.subheader("Download Filtered Data")

csv_buffer = io.StringIO()
filtered_df.to_csv(csv_buffer, index=False)
csv_data = csv_buffer.getvalue()

st.download_button(
    label="⬇️ Download CSV",
    data=csv_data,
    file_name="filtered_data.csv",
    mime="text/csv"
)

excel_buffer = io.BytesIO()
with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
    filtered_df.to_excel(writer, index=False, sheet_name="Filtered Data")

st.download_button(
    label="⬇️ Download Excel",
    data=excel_buffer.getvalue(),
    file_name="filtered_data.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)