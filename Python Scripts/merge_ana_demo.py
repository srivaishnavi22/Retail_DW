import pandas as pd

# Load the first CSV file and pick specific columns
df1 = pd.read_csv('Data\Demographics\DEMO.csv', usecols=['STORE', 'AGE9', 'AGE60'])

# Convert STORE to integer, dropping rows where STORE is null or cannot be converted
df1['STORE'] = pd.to_numeric(df1['STORE'], errors='coerce')  # Convert to numeric, set invalid parsing to NaN
df1.dropna(subset=['STORE'], inplace=True)  # Drop rows where STORE is NaN
df1['STORE'] = df1['STORE'].astype(int)  # Convert STORE to integer

# Load the second CSV file
df2 = pd.read_csv('extract-csv\merged_ana.csv')

# Convert STORE to integer, dropping rows where STORE is null or cannot be converted
df2['STORE'] = pd.to_numeric(df2['STORE'], errors='coerce')  # Convert to numeric, set invalid parsing to NaN
df2.dropna(subset=['STORE'], inplace=True)  # Drop rows where STORE is NaN
df2['STORE'] = df2['STORE'].astype(int)  # Convert STORE to integer

# Merge the two DataFrames on the STORE column
merged_df = pd.merge(df1, df2, on='STORE', how='right')

# Save the merged DataFrame to a new CSV file if needed
merged_df.to_csv('extract-csv\merge_ana_demo.csv', index=False)

# Display the merged DataFrame
print(merged_df)
