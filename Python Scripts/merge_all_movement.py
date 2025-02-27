import os
import pandas as pd

def merge_csvs_incrementally(folder_path, output_file):
    # Check if output file exists, and if so, remove it (to avoid appending to an old file)
    if os.path.exists(output_file):
        os.remove(output_file)

    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is a CSV
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            
            # Load the CSV file
            try:
                df = pd.read_csv(file_path)
                
                # Add a new column for the file name
                df['FILENAME'] = file_name
                
                # Write to output file in append mode, without header if it already exists
                df.to_csv(output_file, mode='a', index=False, header=not os.path.exists(output_file))
                print(f"Appended data from {file_name} to {output_file}")
                
            except Exception as e:
                print(f"Error processing {file_name}: {e}")

# Specify the folder containing CSV files and the output file name
folder_path = "Data\Movement"
output_file = "extract-csv\merge_all_movement.csv"
merge_csvs_incrementally(folder_path, output_file)
