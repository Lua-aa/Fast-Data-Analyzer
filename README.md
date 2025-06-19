# Fast Data Analyzer

**Fast Data Analyzer** is a fast and flexible web application built with Streamlit for interactive data exploration, filtering, and visualization. It allows users to easily upload CSV or Excel files, filter the data dynamically, visualize insights through interactive charts, and download the filtered data.

## Features

- **Upload your data**: Supports CSV and Excel files.
- **Dynamic data filtering**: Filter data based on numerical and categorical columns.
- **Interactive visualizations**: Choose between Bar Charts, Line Charts, Scatter Plots, Pie Charts, and Histograms.
- **Download filtered data**: Save your filtered data as CSV or Excel files.
- **Fast and user-friendly**: Built with performance and simplicity in mind.

## Installation


### 1. Clone the repository

```bash
git clone https://github.com/your-username/Fast-Data-Analyzer.git
cd Fast-Data-Analyzer
```

### 2. Install dependencies

It's recommended to use a **virtual environment** to keep dependencies isolated.

```bash
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

### 1. Run the app

After installing the dependencies, you can run the app locally:

```bash
streamlit run app.py
```

### 2. Upload your data

You can upload a **CSV** or **Excel** file using the file uploader in the sidebar.

### 3. Filter and visualize your data

Use the sidebar to apply filters to your data based on the available columns. You can select different chart types for visualizing your data (Bar, Line, Scatter, Pie, or Histogram).

### 4. Download filtered data

After applying filters, you can download the filtered data as a CSV or Excel file directly from the interface.

---

## Technologies Used

- **Streamlit**: Framework for building the web app.
- **Pandas**: Data manipulation and analysis.
- **Plotly**: Interactive visualizations.
- **OpenPyXL**: Read and write Excel files.
- **Python 3.x**: Programming language.
