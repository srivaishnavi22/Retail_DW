import os
import csv
import json

# Define the folder path containing the CSV files
folder_path = 'Data/Movement'
upc_map = {}

# Iterate over each CSV file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                
                # Read the first row to get the headers
                headers = next(reader)
                
                # Check for 'UPC' or "'UPC'" in headers
                if 'UPC' in headers:
                    upc_column = 'UPC'
                elif "'UPC'" in headers:
                    upc_column = "'UPC'"
                else:
                    print(f"'UPC' column not found in {filename}")
                    continue
                
                # Get the index of the UPC column
                upc_index = headers.index(upc_column)
                
                # Initialize list to store UPC values for the current file
                upc_values = []
                
                # Iterate over each row to collect UPC values
                for row in reader:
                    try:
                        upc_value = row[upc_index]
                        
                        # Skip if UPC value is empty
                        if upc_value == '':
                            continue
                        
                        # Append UPC value to the list
                        upc_values.append(upc_value)
                        
                    except IndexError:
                        print(f"Row has fewer columns than expected in {filename}")
                        continue
                
                # Store the list of UPC values in the dictionary with the filename as the key
                upc_map[filename] = upc_values
        
        except Exception as e:
            print(f"An error occurred with {filename}: {e}")

# Save the UPC map to a JSON file
with open('upc_map.json', 'w') as json_file:
    json.dump(upc_map, json_file, indent=4)

print("UPC map has been saved to upc_map.json")
