# CSV Data Quality Checker

A Python tool that analyzes CSV files and generates a Data Quality Report to help identify common data issues before starting data analysis.

## Project Overview

The CSV Data Quality Checker provides an automated way to inspect CSV datasets and understand their quality.

It generates a report containing important information about the dataset, including missing values, duplicate rows, data types, and numerical statistics.

## Features

- **Dataset Overview:** Displays the total number of rows and columns.
- **Missing Values Analysis:** Identifies missing values in each column and calculates their percentages.
- **Duplicate Detection:** Counts duplicate rows.
- **Data Types Inspection:** Displays the data type of each column.
- **Numerical Statistics:** Provides descriptive statistics for numerical columns.
- **Report Export:** Saves the data quality report as a text file.
- **Error Handling:** Handles common CSV reading errors.

## Technologies Used

- Python
- Pandas
- OS Module
- Datetime Module

## Project Structure

```text
CSV-Data-Quality-Checker/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── sample_data/
│   └── sales.csv
│
└── reports/
    └── data_quality_report.txt
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MariamAhmed61/CSV-Data-Quality-Checker.git
```

2. Navigate to the project folder:

```bash
cd CSV-Data-Quality-Checker
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## How to Use

1. Run the Python script:

```bash
python main.py
```

2. Enter the path of the CSV file when prompted.

3. The program analyzes the dataset and generates a data quality report.

4. Find the generated report inside the `reports` folder.

## Output

The generated report includes:

- Dataset dimensions
- Missing values and percentages
- Duplicate rows count
- Column data types
- Numerical descriptive statistics

## Future Improvements

- Detect inconsistent values.
- Add customizable data validation rules.
- Export reports to PDF or Excel.
- Add a graphical user interface.

## Author

**Mariam Ahmed**

Computer and Systems Engineering Graduate | Junior Data Analyst

GitHub: [MariamAhmed61](https://github.com/MariamAhmed61)
