import pandas as pd
from datetime import datetime

# Load CSV file into DataFrame
file_path = 'Data\Ccount\CCOUNT.csv'  # Update with your file path
df = pd.read_csv(file_path)

# Assuming the date column is named 'DATE' and it's in the format '880101'
def is_numeric(value):
    """Check if the date is numeric and has exactly 6 characters."""
    if len(str(value)) == 6:
        try:
            int(value)
            return True
        except ValueError:
            return False
    return False

def parse_date(date_str):
    """Convert date of type '880101' into '1988-01-01'."""
    if not isinstance(date_str, str):
        if isinstance(date_str, float):
            date_str = str(int(date_str))
        else:
            if isinstance(date_str, int):
                date_str = str(date_str)
    year = int(date_str[:2]) + 1900
    month = int(date_str[2:4])
    day = int(date_str[4:])
    return datetime(year, month, day)

# Filter out non-numeric dates
df = df[df['DATE'].apply(is_numeric)]

# Convert the date column from string to datetime format
df['parsed_date'] = df['DATE'].apply(parse_date)

# Filter rows between 1988 and 1998
df = df[(df['parsed_date'].dt.year >= 1988) & (df['parsed_date'].dt.year <= 1998)]

# Create new columns: year, month, week number, and day of the week
df['year'] = df['parsed_date'].dt.year
df['month'] = df['parsed_date'].dt.month
df['week_number'] = df['parsed_date'].dt.isocalendar().week
df['day_of_week'] = df['parsed_date'].dt.day_name()

# Drop the original date column (optional)
df.drop(columns=['DATE'], inplace=True)

# Create a sales column that sums all columns except 'STORE', 'parsed_date', 'WEEK'
# Identify the columns to sum by excluding non-sales columns
sales_columns = [col for col in df.columns if col not in ['STORE', 'parsed_date', 'WEEK', 'year', 'month', 'week_number', 'day_of_week']]

# Convert the relevant columns to float before summing
df[sales_columns] = df[sales_columns].apply(pd.to_numeric, errors='coerce')  # Convert to float, 'coerce' will turn non-convertible values to NaN

# Sum the sales columns and create the 'sales' column
df['sales'] = df[sales_columns].sum(axis=1)

# Show the final DataFrame
print(df[['STORE', 'parsed_date', 'sales']].head())

# Optionally save the cleaned data back to a CSV file
df.to_csv('extract-csv\extract_ccount_weekofday.csv', index=False)
