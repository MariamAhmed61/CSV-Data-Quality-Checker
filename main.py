
import pandas as pd

print("=" * 40)
print("       CSV DATA QUALITY CHECKER")
print("=" * 40)

# Get CSV file path
file_path = input("Enter CSV file path: ")

try:
    # Read the CSV file
    df = pd.read_csv(file_path)

    print("\n========== DATA OVERVIEW ==========")

    # Display basic information
    print("Total Rows:", df.shape[0])
    print("Total Columns:", df.shape[1])

    print("\n========== MISSING VALUES ==========")

    missing_values = df.isnull().sum()
    print(missing_values)

    print("\nTotal Missing Values:", df.isnull().sum().sum())

    print("\n========== DUPLICATE ROWS ==========")

    duplicates = df.duplicated().sum()
    print("Duplicate Rows:", duplicates)

    print("\n========== DATA TYPES ==========")

    print(df.dtypes)

    print("\n========== BASIC STATISTICS ==========")

    print(df.describe())

    print("\nData Quality Check Completed!")

except FileNotFoundError:
    print("Error: File not found!")

except Exception as e:
    print("An error occurred:", e)
