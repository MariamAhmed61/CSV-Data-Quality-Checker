
import pandas as pd
import os
from datetime import datetime

print("=" * 40)
print("       CSV DATA QUALITY CHECKER")
print("=" * 40)

file_path = input("Enter CSV file path: ")

try:
    # Read CSV file
    df = pd.read_csv(file_path)

    # Basic information
    total_rows = df.shape[0]
    total_columns = df.shape[1]

    # Missing values
    missing_values = df.isnull().sum()
    total_missing = missing_values.sum()

    # Missing percentage
    missing_percentage = (missing_values / total_rows * 100) if total_rows > 0 else missing_values * 0

    # Duplicate rows
    duplicates = df.duplicated().sum()

    # Data types
    data_types = df.dtypes

    # Numeric statistics
    numeric_data = df.select_dtypes(include="number")

    # Build report
    report = []

    report.append("=" * 50)
    report.append("          DATA QUALITY REPORT")
    report.append("=" * 50)

    report.append(f"\nFile Name: {os.path.basename(file_path)}")
    report.append(f"Report Date: {datetime.now()}")

    report.append("\n========== DATA OVERVIEW ==========")
    report.append(f"Total Rows: {total_rows}")
    report.append(f"Total Columns: {total_columns}")

    report.append("\n========== MISSING VALUES ==========")

    missing_report = pd.DataFrame({
        "Missing Values": missing_values,
        "Missing Percentage": missing_percentage.round(2)
    })

    report.append(missing_report.to_string())
    report.append(f"\nTotal Missing Values: {total_missing}")

    report.append("\n========== DUPLICATE ROWS ==========")
    report.append(f"Duplicate Rows: {duplicates}")

    report.append("\n========== DATA TYPES ==========")
    report.append(data_types.to_string())

    report.append("\n========== BASIC STATISTICS ==========")

    if not numeric_data.empty:
        report.append(numeric_data.describe().to_string())
    else:
        report.append("No numeric columns found.")

    report.append("\n========== END OF REPORT ==========")

    # Create reports folder
    os.makedirs("reports", exist_ok=True)

    # Save report
    report_path = os.path.join("reports", "data_quality_report.txt")

    with open(report_path, "w", encoding="utf-8") as file:
        file.write("\n".join(report))

    print("\nData Quality Check Completed!")
    print("Report saved successfully!")
    print("Report Location:", report_path)

except FileNotFoundError:
    print("Error: File not found!")

except pd.errors.EmptyDataError:
    print("Error: CSV file is empty!")

except pd.errors.ParserError:
    print("Error: Unable to parse CSV file!")

except Exception as e:
    print("An error occurred:", e)
