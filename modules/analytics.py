import pandas as pd
import matplotlib.pyplot as plt

try:
    import seaborn as sns
    sns.set()
except ImportError:
    print("Warning: seaborn not installed — plots will look basic.")
    sns = None


                                         #This makes the plot look better with seaborn defaults

def eda_summary(df) :                              #We are making a function called eda sumamry on the df file
                                                   #Here we are printing basic info about our data
                                                   #df.info         ---> Basic info about the data structure and all
                                                   #df.describe().T ---> We print our numeric stats here and we transpose for easier reading
                                                   #df.isnull().sum ---> We print missing values per coloumn

    print("\n--- Info On Our Data ---")
    print(df.info())                               #We are just printing the structure and type here about our data

    print("\n--- Let's DESCRIBE (numeric)---")
    print(df.describe().T)                         #Syntax to print numeric stats, we also have done transposed(T) on it for easier reading

    print("\n---Missing Values Per Coloumn")
    print(df.isnull().sum())                       #Count of missing values per coloumn



def numeric_aggregates(df, numeric_cols):
    """
    For each numeric column print mean, median, std, min and max.
    """
    print("\n--- NUMERIC AGGREGATES ---")
    for col in numeric_cols:                                           #Think of this as checking each numeric coloumn one by one
        series = df[col]                                               #This means that (series) is gonna hold all the values from coloumns in dataframe
        print(f"\nColumn: {col}")                       
        print(f"  count: {series.count()}")                            #{series.count()}  ----> Gets us a count of the coloumns
        print(f"  mean: {series.mean()}")                              #{series.mean()}   ----> Gets us the average value
        print(f"  median: {series.median()}")                          #{series.median()} ----> Gets us the middle value if you sort all numbers
        print(f"  std: {series.std()}")                                #{series.std()}    ----> Gets us the standard deviation, tells how spread out the numbers are 
        print(f"  min: {series.min()}")                                #{series.min()}    ----> Gives us the smallest number
        print(f"  max: {series.max()}")                                #{series.max()}    ----> Gives us the biggest number



def categorical_value_counts(df, categorical_cols, top_n=5):
    """
    For each categorical column show the top N most frequent values and their counts.
    """

    print("\n--- CATEGORICAL VALUE COUNTS ---")
    for col in categorical_cols:                            
        print(f"\nColumn: {col}")
        print(df[col].value_counts(dropna=False).head(top_n))          #Counts how many times each value has appears, its basically counting what's the most common in each coloumn


def correlation_matrix(df, numeric_cols):
    """
    Compute and print the correlation matrix for numeric columns and also plot a heatmap.
    """
    if not numeric_cols:
        print("\n No numeric columns to compute correlation.")          #Basically a loop, where if we dont have any numeric coloumns
        return


    """

        
THIS LOOKS AT ALL THE NUMERIC COLOUMNS, AND TELLS US HOW CLOSELY THEY ARE RELATED TO EACH OTHER
It prints a table of correlation numbers-
    +1 perfect positive correlation
    -1 perfect negative correlation
    0 perfect no correlation

Imagine you’re comparing height and weight of kids:

    If taller kids usually weigh more, the correlation is high (+).

    If taller kids weigh less, correlation is negative (-).

    If height and weight don’t relate, correlation is 0.

    """
            
    corr = df[numeric_cols].corr()
    print("\n--- CORRELATION MATRIX ---")
    print(corr)

    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()


def plot_distributions(df, numeric_cols, max_plots=10):
    """
    Plot histograms (with KDE) for numeric columns. Limits to max_plots to avoid too many figures.

    Draws histograms for numeric columns to show how values are spread.

    Adds a KDE line which is a smooth curve showing density.

    Limits to max_plots so it doesn’t make too many graphs.

    Easier analogy:
    Think of stacking blocks by height:

    Taller stacks mean more numbers fall in that range.

    The KDE is like a smooth line showing where most blocks are.
    """
    plotted = 0
    for col in numeric_cols:
        if plotted >= max_plots:
            break
        plt.figure(figsize=(6,4))
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()
        plotted += 1


def plot_categorical_counts(df, categorical_cols, max_plots=10):
    """
    Plot bar charts for categorical column value counts (top 10 by default).

    Draws bar charts for top values in categorical columns.

    Only shows top 10 most common values by default.

    In simple words:
    Think of stacking different toys by type:

    The tallest bars show which toys you have the most of.

    Each bar = how many of that toy.    
    """
    plotted = 0
    for col in categorical_cols:
        if plotted >= max_plots:
            break
        plt.figure(figsize=(8,4))
        vc = df[col].value_counts().nlargest(10)
        sns.barplot(x=vc.values, y=vc.index)
        plt.title(f"Top values in {col}")
        plt.xlabel("Count")
        plt.ylabel(col)
        plt.tight_layout()
        plt.show()
        plotted += 1


def run_all(df, column_types):
    """
    Convenience function to run a standard suite of analytics.
    """
    numeric = column_types.get("numeric", [])
    categorical = column_types.get("categorical", [])

    eda_summary(df)
    numeric_aggregates(df, numeric)
    categorical_value_counts(df, categorical)
    correlation_matrix(df, numeric)
    plot_distributions(df, numeric)
    plot_categorical_counts(df, categorical)
