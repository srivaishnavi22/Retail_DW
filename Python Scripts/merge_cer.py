import pandas as pd

# Load the first CSV file
df1 = pd.read_csv('Data/Movement/WCER/wcer.csv')

# Load the second CSV file
df2 = pd.read_csv('Data/UPC/UPCCER.csv')

# Merge the two DataFrames on the 'UPCs' column
merged_df = pd.merge(df1, df2, on='UPC', how='left')

# Save the merged DataFrame to a new CSV file if needed
merged_df.to_csv('extract-csv/merge_cer.csv', index=False)

# Display the merged DataFrame
print(merged_df)
