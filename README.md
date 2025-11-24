# AutoMaid
Data’s personal maid

# OBJECTIVE

Objective:

To create an automated data analytics tool that simplifies the initial steps of data analysis, allowing users to quickly understand and explore any dataset without manual effort.

Key Features (MVP):

1. Data Input & Validation
    - Accept CSV or Excel files.
    - Automatically detect file type, encoding, and load into a DataFrame.
    - Handle common issues like missing files, wrong delimiters, or empty columns.
2. Automated Data Cleaning
    - Identify missing values and duplicates.
    - Impute missing data intelligently (mean/median/mode depending on column type).
    - Convert data types appropriately and encode categorical variables.
3. Exploratory Data Analysis (EDA)
    - Generate summaries of numeric and categorical variables.
    - Visualize distributions (histograms, boxplots) and correlations.
    - Provide a concise summary of dataset insights (e.g., most correlated features, key stats).

Tech Stack:

- Python Libraries: pandas, numpy, matplotlib, seaborn
- Optional for faster EDA: ydata-profiling

Outcome:

A user can upload any dataset and get an automatically cleaned and analyzed version, with visualizations and summaries, ready for further analysis or modeling.




# **What we did?**

We built a **modular EDA (Exploratory Data Analysis) pipeline** in Python with three main modules:

- **data_input.py** – Loads data from CSV/Excel and prints a success message with row/column counts.
- **event_processing.py** – Prepares the data:
    - Cleans column names (lowercase, replace spaces with `_`)
    - Handles missing values (drops rows that are mostly empty)
    - Detects column types (numeric vs categorical)
- **analytics.py** – Runs the actual analysis:
    - Prints basic dataframe info (`df.info()`)
    - Describes numeric statistics (`df.describe().T`)
    - Counts missing values per column
    - Computes aggregates for numeric columns (mean, median, min, max, std)
    - Counts top values in categorical columns
    - Computes and prints the correlation matrix and shows a heatmap
    - Plots histograms for numeric columns with KDE
    - Plots bar charts for top categorical values

Finally, **main.py** ties everything together: loads the data → prepares it → runs analytics.

**💡 Empty `__init__.py` file:**

This file is intentionally empty but necessary—it **tells Python that the `modules` folder is a package**, allowing you to import modules like `from modules.analytics import run_all`.

---

# **What our current summary looks like**

For your Titanic dataset:

- **Basic info:** 891 rows, 12 columns, with `age` and `cabin` having missing values.
- **Numeric stats:** Count, mean, median, std, min, max for columns like `age`, `fare`, `sibsp`, etc.
- **Categorical counts:** Top values for `sex`, `embarked`, `ticket`, `cabin`, etc.
- **Correlation matrix:** Shows correlations among numeric columns (like `fare` vs `pclass`)
- **Plots:** Histograms for numeric columns and bar charts for top categorical values

So basically, you now have a **full snapshot of your dataset** in both text (terminal) and visuals (plots).

---

# **How we can make it better later**

- Later, we can make the program more user-friendly so you can **drag and drop your CSV/Excel file**, instead of hardcoding the file path.
- **Missing values analysis:** Show % missing and visualize with heatmaps or bar charts.
- **Datetime handling:** Detect and convert date columns for time-based analysis.( We already commented out the block of code as we havent declared it in the [main.py](http://main.py) yet)
- **Outlier detection:** Boxplots or z-score filtering for numeric columns.
- **Automated reports:** Generate HTML or PDF reports with plots and tables.
- **Customizable plots:** Allow users to select which columns to visualize or save plots automatically.
- **Categorical encoding:** For machine learning preparation.
- **Interactive visualizations:** Use Plotly or Dash for dynamic charts.
- **Summary metrics:** Add skewness, kurtosis, or unique value counts for more insight.

---

**💡 In short:**

We now have a **modular EDA pipeline** that gives a clean, structured summary of your data with numeric stats, missing values, categorical value counts, correlations, and visualizations. Later, it can be extended to be **interactive, automated, drag-and-drop ready, and ML-prepared**.
