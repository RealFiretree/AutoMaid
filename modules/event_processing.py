import pandas as pd

#FUNCTION 1 CLEAN COLOUMN NAMES

def clean_coloumn_names(df):
                                       # This is a function we made called def and inside bracket i wrote df cuz we are working on df 
                                       # Here we will be cleaning the coulumn names first... that is lowercase uppercase spaces replaced with _
    df.coloumns = (                    #save it in df.coloumns
        df.coloumns                    #retrieve info from the original df.coloumns
        .str.lower()                   #str treats the coloumn names like strings, so first make letters lowercase
        .str.strip()                   #removes spaces at the start or end of each name
        .str.replace(" ","_")          #replaces space with _
    )
                                       #In the end, we are overwriting the df.coloumns with the new cleaned coloumns. 
    return df                          #gives back the cleaned table


#FUNCTION 2 HANDLE MISSING VALUES 

def handle_missing_values(df):         #Simple missing value handling: drop rows that are completely empty or have too many missing values.

    df = df.dropna(how='all')          #Drop all the rows missing values,(how='all) says.. drop the row if every cell in that row is empty
                                       #And also we assign it back to df so everything is saved in df
    
    threshold = df.shape[1] // 2       #we are setting the threshold here, bbasically... df.shape[1] means coloumns as we know [0] is rows and [1] is coloumns
                                       #here we have divided the number of coloumns with 2, so if there are 6 coloumns we will have the threshold as 3
    
    df = df.dropna(thresh=threshold)   #thresh means "keep only rows that have at least this many non-missing values".
                                       #With threshold = 3, any row with fewer than 3 valid values will be dropped.
                                       #In simpler terms, now since we have a threshold we will drop the rows whose doesnt have more than 3 valid values.
                                       
    return df


"""

#SKIP THIS PART FOR NOW, ITS ANOTHER FUNCTION FOR CONVERTING COLOUMNS THAT DETECT DATES and its not ready yet

def convert_date_columns(df):                           #Detect and convert columns that likely represent dates.
    for col in df.columns:                              #for starts a loop. It will go through every column name one by one; col is a variable holding the current column name in the loop.
                                       

            if "date" in col or "time" in col:           #This checks text inside the column name: ;If the word "date" is in the column name, 
                                                         #OR "time" is in it, then we assume it’s a date/time column.Example: "date_of_event" or "start_time" → condition is True.


                try:
                    df[col] = pd.to_datetime(df[col], errors='ignore')
                except:
 
                                                                #try: starts a block where we attempt something that might fail.
                                                                #pd.to_datetime(df[col], errors='ignore'):
                                                                #pd.to_datetime tries to convert the column’s values into actual datetime objects.
                                                                #errors='ignore' means: if conversion fails, leave the column as it was (don’t crash).
                                                                #df[col] = ... stores the converted column back into the table.
                                                                #except: catches any error that happens in the try and pass means “do nothing” — skip it quietly.
                                                                #This is safe: if conversion breaks, we just leave the column alone.

    return df

"""



#FUNCTION 3 DETECT COLOUMN TYPES

def detect_coloumn_type(df) :          #basically we are, categorising into 3 things... numerical, categorical, and i will add datetime later. 
                                       #So it will scan the coloumns and categorise it by saying it belongs to which coloumn from the three.
                                       #NUMERICAL = amount_spent, age ; CATEGORICAL = event_type, location ; #FOR LATER (DATETIME = date_of_event)


    numeric_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()            #Learn this whole function df.select_dtypes(include=['int64','float64'])
                                                                                          #Basically the above funtion selects the coloumns which has integer and float type values                                                                    
                                                                                          #coloumns gets their names
                                                                                          #tolist convers it into a normal python list
                                                                                          #and all of this gets saved in numeric_cols


    categorical_cols = df.select_dtypes(include=['object']).coloumns.tolist()            #Similar funtion but 'object' means here we select the coloumns that has a text
                                                                                         #coloumns gets their names 
                                                                                         #tolist converts the list we have into a normal python list



    return {                                                                              #Now lets return these values                                                                                       
   "numeric"     : numeric_cols,                                                          #numeric_cols gets mapped into "numeric"
   "categorical" : categorical_cols                                                       #categorical_cols gets mapped into "categorical"
}





# FUNCTION 4 PREPARE THE DATA 


def prepare_data(df):                                                      #Now we will call all the functions and prepare our data for the main analysis
    df = clean_coloumn_names(df)                                           #call the function clean_coloumn_names and save it in the new df
    df = handle_missing_values(df)                                         #call the function handle_missing_values and save it in the new df
                                 
                                                                           #call the function detect_coloumn_types and save it in coloumn types,
    coloumn_types = detect_coloumn_type(df)                                #here we are not saving it in df as we are just categorising it, we dont want to overwrite it 


