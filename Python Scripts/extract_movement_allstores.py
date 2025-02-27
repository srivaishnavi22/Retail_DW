import os
import csv

# Root directory containing folders with CSV files
root_directory = 'Data\Movement'

# List to store matched rows
matched_rows = []

# Recursively iterate over all subdirectories and files
for dirpath, dirnames, filenames in os.walk(root_directory):
    for filename in filenames:
        if filename.endswith(".csv"):
            filepath = os.path.join(dirpath, filename)
            
            # Open and read each CSV file
            with open(filepath, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                
                # Iterate over each row and check if the column values match
                for row in reader:
                    matched_rows.append(row)

# Write matched rows to a new CSV file
output_file = 'extract-csv\extract_movement_allstores.csv'
if matched_rows:
    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=matched_rows[0].keys())
        writer.writeheader()
        writer.writerows(matched_rows)

    print(f"Matched rows written to {output_file}")
else:
    print("No matched rows found.")
