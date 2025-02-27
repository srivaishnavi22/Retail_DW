import pandas as pd
from datetime import datetime, timedelta
import holidays

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

# Add a column for identifying U.S. holidays excluding observed holidays
us_holidays = holidays.US(years=range(1988, 1999))

# Exclude the "Observed" holidays
excluded_holidays = ["Christmas Day (Observed)", "Independence Day (Observed)", 
                     "New Year's Day (Observed)", "Veterans Day (Observed)"]

# Function to return the holiday name if it's not an observed holiday, else None
def get_holiday_name(date):
    holiday_name = us_holidays.get(date)
    if holiday_name and holiday_name not in excluded_holidays:
        return holiday_name
    return None

# Apply the function to add the holiday name or leave it as None
df['holiday_name'] = df['parsed_date'].apply(get_holiday_name)

# Create a dictionary to store week number and the holiday for that week
holiday_weeks = {}

# Identify week number for each holiday and mark entire week as holiday week
for _, row in df[df['holiday_name'].notnull()].iterrows():
    week_num = row['week_number']
    holiday_name = row['holiday_name']
    
    # If the week is not already marked, mark it with the current holiday
    if week_num not in holiday_weeks:
        holiday_weeks[week_num] = holiday_name

# Function to check if a row's week is a holiday week and return the holiday name
def assign_holiday_week(row):
    week_num = row['week_number']
    return holiday_weeks.get(week_num, None)

# Apply the function to mark the entire week as holiday week
df['holiday_week'] = df.apply(assign_holiday_week, axis=1)

# Show the final DataFrame
print(df[['STORE', 'parsed_date', 'sales', 'holiday_name', 'holiday_week']].head())

# Optionally save the cleaned data back to a CSV file
df.to_csv('extract-csv\extract_ccount_holidays.csv', index=False)
