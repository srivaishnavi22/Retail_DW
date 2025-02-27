import os
import csv

# Root directory containing folders with CSV files
root_directory = 'Data/Movement'

# Columns to check and values to match
column1_name = 'SALE'
column2_name = 'STORE'
# match_value1 = 'C'
match_value2 = set(['2','4','5','8','9'])

# Output file path
output_file = 'extract-csv/extract_movement.csv'

# Open the output file once and write matched rows as they are found
with open(output_file, mode='w', newline='') as output_file:
    writer = None  # Declare writer here to use it outside the loop

    # Recursively iterate over all subdirectories and files
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith(".csv"):
                filepath = os.path.join(dirpath, filename)

                # Open and read each CSV file
                with open(filepath, mode='r', newline='') as file:
                    reader = csv.DictReader(file)

                    # Initialize the CSV writer with the header on the first file
                    if writer is None:
                        writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
                        writer.writeheader()

                    # Iterate over each row and write it directly to the output file if it matches
                    for row in reader:
                        try:
                            # Add your condition to filter rows if necessary
                            if row[column2_name] in match_value2:
                                writer.writerow(row)
                        except Exception as e:
                            print(f"Failed to write row: {row}")
                            print(f"Error: {e}")

print(f"Processed files and written matched rows to {output_file}")
