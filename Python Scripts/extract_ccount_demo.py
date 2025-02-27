import pandas as pd

# Load the first CSV file
csv_file1 = 'extract-csv\extract_ccount_weekofday.csv'
df1 = pd.read_csv(csv_file1)

# Load the second CSV file
csv_file2 = 'Data\Demographics\DEMO.csv'
df2 = pd.read_csv(csv_file2)

# Check if the 'store' column has numeric values and remove non-numeric rows
df1 = df1[pd.to_numeric(df1['STORE'], errors='coerce').notna()]
df2 = df2[pd.to_numeric(df2['STORE'], errors='coerce').notna()]

# Convert the 'store' column to int in both DataFrames after ensuring valid numeric entries
df1['STORE'] = df1['STORE'].astype(int)
df2['STORE'] = df2['STORE'].astype(int)

# Perform an inner join on the 'store' column
# You can modify this to 'left', 'right', or 'outer' depending on your join type
merged_df = pd.merge(df1, df2, on='STORE', how='inner')

# Save the result to a new CSV file
output_file = 'extract-csv\merge_ccount_demo.csv'
merged_df.to_csv(output_file, index=False)

print(f"Merged data saved to {output_file}")
