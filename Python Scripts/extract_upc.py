import os
import csv

# Directory containing the CSV files
directory = 'Data/UPC'

# List to store all rows from all CSV files
all_rows = []

# Iterate over all CSV files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        filepath = os.path.join(directory, filename)
        
        # Open and read each CSV file
        with open(filepath, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            print(file)
            # Get fieldnames (column headers) from the first CSV
            if not all_rows:
                fieldnames = reader.fieldnames + ['group_name']  # Add new column 'source_file'
                
            # Iterate over each row, add filename as a new column and store the row
            for row in reader:
                # Skip rows with None values (if any)
                if None not in row.values():
                    row['group_name'] = filename  # Add CSV filename to each row
                    all_rows.append(row)

# Write all the rows with the 'source_file' column to a new CSV file
output_file = 'extract-csv\extract_upc.csv'
if all_rows:
    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"All rows combined and written to {output_file}")
else:
    print("No rows found.")
