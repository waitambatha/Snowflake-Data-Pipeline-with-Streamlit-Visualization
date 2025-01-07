# **Snowflake Data Pipeline with Streamlit Visualization**

This project demonstrates how to:
1. Fetch JSON data from a public API.
2. Load the data into Snowflake.
3. Automatically create a table in Snowflake based on the JSON structure.
4. Visualize the data using **Streamlit** and **Plotly**.

The project includes **10 different types of visualizations** to explore and analyze the data interactively.

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Setup Instructions](#setup-instructions)
5. [Running the Project](#running-the-project)
6. [Fetching and Loading Data into Snowflake](#fetching-and-loading-data-into-snowflake)
7. [Visualizations](#visualizations)
8. [Troubleshooting](#troubleshooting)
9. [Contributing](#contributing)
10. [License](#license)

---

## **Project Overview**

This project automates the process of:
1. Fetching JSON data from a public API.
2. Loading the data into Snowflake.
3. Dynamically creating a table in Snowflake based on the JSON structure.
4. Building an interactive web app using **Streamlit** to visualize the data with **Plotly**.

---

## **Features**

- **Automated Data Pipeline**:
  - Fetches JSON data from a public API.
  - Loads the data into Snowflake.
  - Dynamically creates a table based on the JSON structure.

- **Interactive Visualizations**:
  - Provides **10 different types of visualizations** using Plotly:
    1. Bar Chart
    2. Line Chart
    3. Scatter Plot
    4. Histogram
    5. Pie Chart
    6. Box Plot
    7. Violin Plot
    8. Area Chart
    9. Heatmap
    10. 3D Scatter Plot

- **User-Friendly Interface**:
  - Allows users to select columns dynamically for each visualization.
  - Displays raw data and column names for debugging.

---

## **Prerequisites**

Before running the project, ensure you have the following:

1. **Python 3.8+** installed.
2. **Snowflake Account** with a warehouse, database, and schema.
3. **Streamlit** and other required Python libraries installed.
4. A **public JSON dataset** (e.g., from a public API).

---

## **Setup Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/waitambatha/snowflake-streamlit-project.git
   cd snowflake-streamlit-project
   ```

2. **Install Required Libraries**:
   ```bash
   pip install streamlit snowflake-connector-python pandas plotly python-dotenv
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the project directory with the following content:
     ```plaintext
     SNOWFLAKE_USER=your_username
     SNOWFLAKE_PASSWORD=your_password
     SNOWFLAKE_ACCOUNT=your_account_identifier
     SNOWFLAKE_WAREHOUSE=your_warehouse
     SNOWFLAKE_DATABASE=your_database
     SNOWFLAKE_SCHEMA=your_schema
     ```
   - Replace the placeholders with your actual Snowflake credentials.

4. **Update the Script**:
   - Replace the JSON data URL in the script with your desired dataset.

---

## **Running the Project**

1. **Run the Streamlit App**:
   ```bash
   streamlit run snowflake_streamlit_app.py
   ```

2. **Interact with the App**:
   - The app will open in your browser.
   - Select columns dynamically for each visualization.
   - Explore the data using the interactive charts.

---

## **Fetching and Loading Data into Snowflake**

The project includes a Python script (`upload_json_to_snowflake.py`) that:
1. Fetches JSON data from a public API.
2. Connects to Snowflake.
3. Dynamically creates a table (`dynamic_table`) based on the JSON structure.
4. Loads the data into the table.

### **Steps to Fetch and Load Data**

1. **Fetch JSON Data**:
   - The script fetches JSON data from a public API (e.g., `https://data.ny.gov/api/views/5xaw-6ayf/rows.json?accessType=DOWNLOAD`).

2. **Connect to Snowflake**:
   - The script uses the `snowflake-connector-python` library to connect to Snowflake using the credentials from the `.env` file.

3. **Create Table Dynamically**:
   - The script infers the schema from the JSON data and creates a table (`dynamic_table`) in Snowflake.

4. **Load Data**:
   - The script inserts the JSON data into the `dynamic_table`.

---

## **Visualizations**

The app provides the following visualizations:

1. **Bar Chart**:
   - Compare values across categories.

2. **Line Chart**:
   - Visualize trends over time.

3. **Scatter Plot**:
   - Explore relationships between two numeric variables.

4. **Histogram**:
   - Analyze the distribution of a numeric variable.

5. **Pie Chart**:
   - Show proportions of a categorical variable.

6. **Box Plot**:
   - Visualize the distribution of a numeric variable by category.

7. **Violin Plot**:
   - Combine a box plot and kernel density plot.

8. **Area Chart**:
   - Visualize trends over time with filled areas.

9. **Heatmap**:
   - Show relationships between two categorical variables using color intensity.

10. **3D Scatter Plot**:
    - Explore relationships between three numeric variables in 3D space.

---

## **Troubleshooting**

1. **No Data Displayed**:
   - Ensure your Snowflake table (`dynamic_table`) contains data.
   - Verify that the selected columns exist and contain valid data.

2. **Incorrect Data Types**:
   - Ensure the selected columns have the correct data types (e.g., numeric for Y-axis, categorical for X-axis).

3. **Connection Issues**:
   - Verify your Snowflake credentials in the `.env` file.
   - Ensure your firewall allows connections to Snowflake.

4. **Debugging**:
   - Use the `st.write(column_names)` and `st.write(df)` statements in the app to inspect the data and column names.

---

## **Contributing**

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

---


## **Acknowledgments**

- **Snowflake** for providing a powerful cloud data platform.
- **Streamlit** for making it easy to build interactive web apps.
- **Plotly** for creating beautiful and interactive visualizations.

---

