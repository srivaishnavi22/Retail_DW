import pandas as pd # type: ignore

upc_dict = {
    'UPCANA.csv': 'Analgesics',
    'UPCBAT.csv': 'Bath Soap',
    'UPCBER.csv': 'Beer',
    'UPCBJC.csv': 'Bottled Juices',
    'UPCCER.csv': 'Cereals',
    'UPCCHE.csv': 'Cheeses',
    'UPCCIG.csv': 'Cigarettes',
    'UPCCOO.csv': 'Cookies',
    'UPCCRA.csv': 'Crackers',
    'UPCCSO.csv': 'Canned Soup',
    'UPCDID.csv': 'Dish Detergent',
    'UPCFEC.csv': 'Front-end-candies',
    'UPCFRD.csv': 'Frozen Dinners',
    'UPCFRE.csv': 'Frozen Entrees',
    'UPCFRJ.csv': 'Frozen Juices',
    'UPCFSF.csv': 'Fabric Softeners',
    'UPCGRO.csv': 'Grooming Products',
    'UPCLND.csv': 'Laundry Detergents',
    'UPCOAT.csv': 'Oatmeal',
    'UPCPTW.csv': 'Paper Towels',
    'UPCRFJ.csv': 'Refrigerated Juices',
    'UPCSDR.csv': 'Soft Drinks',
    'UPCSHA.csv': 'Shampoos',
    'UPCSNA.csv': 'Snack Crackers',
    'UPCSOA.csv': 'Soaps',
    'UPCTBR.csv': 'Toothbrushes',
    'UPCTNA.csv': 'Canned Tuna',
    'UPCTPA.csv': 'Toothpastes',
    'UPCTTI.csv': 'Bathroom Tissues'
}

# Load both CSV files into DataFrames
df1 = pd.read_csv('extract-csv\extract_movement.csv')  # First CSV file
df2 = pd.read_csv('extract-csv\extract_upc.csv')  # Second CSV file

# Add 'category_name' to df1 by mapping the 'UPC.csv' column using the dictionary
df2['category_name'] = df2['group_name'].map(upc_dict)
print(df2.head())

# Check if UPC exists in both CSVs and merge the matching rows
# 'UPC' is the common column used for matching
df_merged = pd.merge(df1, df2, on='UPC', how='left')

# Save the merged DataFrame to a new CSV file
df_merged.to_csv('extract-csv\merge_upc_movement.csv', index=False)

print("Merged CSV saved as 'merged_output.csv'")
