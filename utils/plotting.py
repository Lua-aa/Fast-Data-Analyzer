import plotly.express as px

def create_plot(chart_type, df, x_axis=None, y_axis=None, cat_col=None, num_col=None):
    if chart_type == "Bar Chart":
        return px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} by {x_axis}")
    elif chart_type == "Line Chart":
        return px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} over {x_axis}")
    elif chart_type == "Scatter Plot":
        return px.scatter(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
    elif chart_type == "Pie Chart":
        return px.pie(df, names=cat_col, values=num_col, title=f"Distribution of {num_col} by {cat_col}")
    elif chart_type == "Histogram":
        return px.histogram(df, x=num_col, title=f"Histogram of {num_col}")
    else:
        return None
