import os
import pandas as pd

# Define the folder path containing the CSV files
folder_path = 'Data/Movement'

# Iterate over each CSV file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        
        try:
            # Read the CSV file with error handling for bad lines
            df = pd.read_csv(file_path, header=1, error_bad_lines=False)  # Skip schema row with header=1
            
            # Check if 'UPC' (or "'UPC'") column exists in the file
            if 'UPC' in df.columns or "'UPC'" in df.columns:
                # Handle both column name variations
                upc_column = 'UPC' if 'UPC' in df.columns else "'UPC'"
                
                # Calculate max and min for UPC as strings
                max_upc = df[upc_column].max()
                min_upc = df[upc_column].min()
                
                print(f"For file {filename}:")
                print(f"Max UPC: {max_upc}")
                print(f"Min UPC: {min_upc}\n")
            else:
                print(f"'UPC' column not found in {filename}")
        
        except pd.errors.ParserError as e:
            print(f"Could not parse {filename} due to parsing error: {e}")
