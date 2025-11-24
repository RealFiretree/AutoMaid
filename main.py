from modules.data_input import load_data
from modules.event_processing import prepare_data
from modules.analytics import run_all

# Set the path to your CSV
file_path = r"C:\Users\iamth\OneDrive\Documents\coding\AutoMaid\data\Titanic-Dataset.csv"

# Load data
df = load_data(file_path)

# Prepare data
df, column_types = prepare_data(df)

# Run analytics
run_all(df, column_types)
