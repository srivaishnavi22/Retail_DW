import csv

# Define input and output file paths
input_file = 'Data/UPC/upcrfj.txt'
output_file = 'Data/UPC/UPCRFJ.csv'

# Open the input and output files
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    # Create a CSV writer object
    writer = csv.writer(outfile)
    
    # Iterate over each line in the input file
    for line in infile:
        # Split the line into fields based on whitespace
        fields = line.strip().split()
        # Write the fields as a row in the CSV
        writer.writerow(fields)

print(f"Conversion complete. CSV saved as {output_file}")
