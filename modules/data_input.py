import pandas as pd

def load_data(file_path):
    # Loads a CSV or Excel file and returns a pandas DataFrame. Handles errors and prints useful messages.

    try:
        # FIXED: endswith (you wrote endswitch)
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)  # since its a prototype we are going to stick to file path for now but later we will change it

        elif file_path.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file_path)  # since its a prototype we are going to stick to file path for now but later we will change it

        else:
            raise ValueError("Unsupported Format Please Try Again, Make Sure To Use CSV or Excel ")
        
        # Basically if its .csv -> then read_csv() or if its .xls or .xlsx then read_excel() Else throw an error

        print(f"Data Loaded Successfully : {df.shape[0]} rows, {df.shape[1]} coloumns")
        # Here we are printing the data that we loaded, about the df part... df.shape [rows,coloumns]
        # so here we will get the total number or rows and coloumns

        return df   # FIXED: you forgot to return df

    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None
