import streamlit as st
import snowflake.connector
import pandas as pd
import plotly.express as px
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to connect to Snowflake and fetch data
def fetch_data():
    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        schema=os.getenv('SNOWFLAKE_SCHEMA')
    )
    cursor = conn.cursor()
    query = "SELECT * FROM dynamic_table"
    cursor.execute(query)
    rows = cursor.fetchall()
    column_names = [col[0] for col in cursor.description]  # Get column names
    df = pd.DataFrame(rows, columns=column_names)
    cursor.close()
    conn.close()
    return df, column_names

# Streamlit app
def main():
    st.title("Snowflake Data Visualization with Streamlit")
    st.write("Visualizing data from the `dynamic_table` in Snowflake.")

    # Fetch data from Snowflake
    df, column_names = fetch_data()

    # Display raw data
    st.subheader("Raw Data")
    st.write(df)

    # Display column names for debugging
    st.subheader("Column Names")
    st.write(column_names)

    # Interactive visualizations
    st.subheader("Interactive Visualizations")

    # 1. Bar Chart
    if len(column_names) >= 2:
        st.write("### Bar Chart")
        x_axis = st.selectbox("Select X-axis for Bar Chart", column_names)
        y_axis = st.selectbox("Select Y-axis for Bar Chart", column_names)
        if x_axis and y_axis:
            try:
                fig = px.bar(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
                st.plotly_chart(fig)
            except Exception as e:
                st.error(f"Error creating bar chart: {e}")

    # 2. Line Chart
    if len(column_names) >= 2:
        st.write("### Line Chart")
        x_axis = st.selectbox("Select X-axis for Line Chart", column_names)
        y_axis = st.selectbox("Select Y-axis for Line Chart", column_names)
        if x_axis and y_axis:
            try:
                fig = px.line(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
                st.plotly_chart(fig)
            except Exception as e:
                st.error(f"Error creating line chart: {e}")

    # 3. Scatter Plot
    if len(column_names) >= 2:
        st.write("### Scatter Plot")
        x_axis = st.selectbox("Select X-axis for Scatter Plot", column_names)
        y_axis = st.selectbox("Select Y-axis for Scatter Plot", column_names)
        if x_axis and y_axis:
            try:
                fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
                st.plotly_chart(fig)
            except Exception as e:
                st.error(f"Error creating scatter plot: {e}")

    # 4. Histogram
    if len(column_names) >= 1:
        st.write("### Histogram")
        x_axis = st.selectbox("Select X-axis for Histogram", column_names)
        if x_axis:
            try:
                fig = px.histogram(df, x=x_axis, title=f"Distribution of {x_axis}")
                st.plotly_chart(fig)
            except Exception as e:
                st.error(f"Error creating histogram: {e}")

    # 5. Pie Chart
    if len(column_names) >= 2:
        st.write("### Pie Chart")
        names = st.selectbox("Select Column for Pie Chart Names", column_names)
        values = st.selectbox("Select Column for Pie Chart Values", column_names)
        if names and values:
            try:
                fig = px.pie(df, names=names, values=values, title=f"Distribution of {names}")
                st.plotly_chart(fig)
            except Exception as e:
                st.error(f"Error creating pie chart: {e}")

    # 6. Box Plot
    if len(column_names) >= 2:
        st.write("### Box Plot")
        x_axis = st.selectbox("Select X-axis for Box Plot", column_names)
        y_axis = st.selectbox("Select Y-axis for Box Plot", column_names)
        if x_axis and y_axis:
            try:
                fig = px.box(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
                st.plotly_chart(fig)
            except Exception as e:
                st.error(f"Error creating box plot: {e}")

    # 7. Violin Plot
    if len(column_names) >= 2:
        st.write("### Violin Plot")
        x_axis = st.selectbox("Select X-axis for Violin Plot", column_names)
        y_axis = st.selectbox("Select Y-axis for Violin Plot", column_names)
        if x_axis and y_axis:
            try:
                fig = px.violin(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
                st.plotly_chart(fig)
            except Exception as e:
                st.error(f"Error creating violin plot: {e}")

    # 8. Area Chart
    if len(column_names) >= 2:
        st.write("### Area Chart")
        x_axis = st.selectbox("Select X-axis for Area Chart", column_names)
        y_axis = st.selectbox("Select Y-axis for Area Chart", column_names)
        if x_axis and y_axis:
            try:
                fig = px.area(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
                st.plotly_chart(fig)
            except Exception as e:
                st.error(f"Error creating area chart: {e}")

    # 9. Heatmap
    if len(column_names) >= 3:
        st.write("### Heatmap")
        x_axis = st.selectbox("Select X-axis for Heatmap", column_names)
        y_axis = st.selectbox("Select Y-axis for Heatmap", column_names)
        values = st.selectbox("Select Values for Heatmap", column_names)
        if x_axis and y_axis and values:
            try:
                pivot_df = df.pivot_table(index=x_axis, columns=y_axis, values=values, aggfunc="sum")
                fig = px.imshow(pivot_df, title=f"Heatmap: {x_axis} vs {y_axis}")
                st.plotly_chart(fig)
            except Exception as e:
                st.error(f"Error creating heatmap: {e}")

    # 10. 3D Scatter Plot
    if len(column_names) >= 3:
        st.write("### 3D Scatter Plot")
        x_axis = st.selectbox("Select X-axis for 3D Scatter Plot", column_names)
        y_axis = st.selectbox("Select Y-axis for 3D Scatter Plot", column_names)
        z_axis = st.selectbox("Select Z-axis for 3D Scatter Plot", column_names)
        if x_axis and y_axis and z_axis:
            try:
                fig = px.scatter_3d(df, x=x_axis, y=y_axis, z=z_axis, title=f"3D Scatter Plot: {x_axis} vs {y_axis} vs {z_axis}")
                st.plotly_chart(fig)
            except Exception as e:
                st.error(f"Error creating 3D scatter plot: {e}")

# Run the app
if __name__ == "__main__":
    main()