"""
Complete Python Guide for Data Analysts
Chapter 8: Pandas - Data Manipulation and Analysis
Author: Debashis Sen
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# ============================================================================
# 1. CREATING DATAFRAMES
# ============================================================================

print("=" * 70)
print("1. CREATING DATAFRAMES")
print("=" * 70)

# Method 1: From dictionary
employees_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'Salary': [75000, 60000, 85000, 70000, 62000],
    'Years': [5, 2, 7, 3, 1]
}

df = pd.DataFrame(employees_dict)
print("\nDataFrame from Dictionary:")
print(df)

# Method 2: From list of lists
data = [
    ['Alice', 25, 'IT', 75000],
    ['Bob', 30, 'HR', 60000],
    ['Charlie', 35, 'IT', 85000]
]
df2 = pd.DataFrame(data, columns=['Name', 'Age', 'Department', 'Salary'])
print("\n\nDataFrame from List of Lists:")
print(df2)

# ============================================================================
# 2. BASIC DATAFRAME OPERATIONS
# ============================================================================

print("\n\n" + "=" * 70)
print("2. BASIC DATAFRAME OPERATIONS")
print("=" * 70)

# Shape and dimensions
print(f"\nDataFrame shape: {df.shape}")  # (rows, columns)
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Info about the DataFrame
print("\nDataFrame Info:")
print(df.info())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# ============================================================================
# 3. DATA SELECTION AND INDEXING
# ============================================================================

print("\n\n" + "=" * 70)
print("3. DATA SELECTION AND INDEXING")
print("=" * 70)

# Select single column (returns Series)
print("\nSelect Name column (Series):")
print(df['Name'])

# Select multiple columns (returns DataFrame)
print("\n\nSelect Name and Salary columns (DataFrame):")
print(df[['Name', 'Salary']])

# Select rows by condition
print("\n\nIT Department Employees:")
it_employees = df[df['Department'] == 'IT']
print(it_employees)

# Select rows with salary > 70000
print("\n\nHigh Earners (Salary > 70000):")
high_earners = df[df['Salary'] > 70000]
print(high_earners)

# Multiple conditions
print("\n\nIT Employees with Salary > 75000:")
filtered = df[(df['Department'] == 'IT') & (df['Salary'] > 75000)]
print(filtered)

# Using .query() method
print("\n\nUsing .query() method:")
result = df.query("Department == 'IT' and Salary > 75000")
print(result)

# Using .loc[] (label-based)
print("\n\nUsing .loc[] - Get rows where Department is IT:")
print(df.loc[df['Department'] == 'IT'])

# Using .iloc[] (position-based)
print("\n\nUsing .iloc[] - First 3 rows:")
print(df.iloc[0:3])

# ============================================================================
# 4. DATA CLEANING
# ============================================================================

print("\n\n" + "=" * 70)
print("4. DATA CLEANING")
print("=" * 70)

# Create DataFrame with missing values
data_with_nan = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [25, 30, None, 28, 32],
    'Salary': [75000, None, 85000, 70000, 62000],
    'Department': ['IT', 'HR', 'IT', None, 'HR']
}
df_dirty = pd.DataFrame(data_with_nan)
print("\nDataFrame with Missing Values:")
print(df_dirty)

# Check for missing values
print("\n\nMissing Values:")
print(df_dirty.isnull())

# Count missing values
print("\n\nCount of Missing Values per Column:")
print(df_dirty.isnull().sum())

# Drop rows with any missing value
print("\n\nAfter Dropping Rows with Any NaN:")
df_clean1 = df_dirty.dropna()
print(df_clean1)

# Drop rows with all missing values
print("\n\nAfter Dropping Rows with All NaN:")
df_clean2 = df_dirty.dropna(how='all')
print(df_clean2)

# Fill missing values
print("\n\nFill Missing Salary with Mean:")
df_filled = df_dirty.copy()
df_filled['Salary'].fillna(df_filled['Salary'].mean(), inplace=True)
print(df_filled)

# Fill with specific value
print("\n\nFill Missing Department with 'Unknown':")
df_filled2 = df_dirty.copy()
df_filled2['Department'].fillna('Unknown', inplace=True)
print(df_filled2)

# Handle duplicates
print("\n\n" + "=" * 70)
print("5. HANDLING DUPLICATES")
print("=" * 70)

df_dup = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'Charlie'],
    'Salary': [75000, 60000, 75000, 85000]
})

print("\nDataFrame with Duplicates:")
print(df_dup)

print("\n\nCheck for Duplicates:")
print(df_dup.duplicated())

print("\n\nRemove Duplicate Rows:")
df_unique = df_dup.drop_duplicates()
print(df_unique)

# ============================================================================
# 6. GROUPBY AND AGGREGATION
# ============================================================================

print("\n\n" + "=" * 70)
print("6. GROUPBY AND AGGREGATION")
print("=" * 70)

# Simple groupby
print("\nAverage Salary by Department:")
avg_salary = df.groupby('Department')['Salary'].mean()
print(avg_salary)

# Multiple aggregations
print("\n\nMultiple Aggregations by Department:")
agg_result = df.groupby('Department').agg({
    'Salary': ['mean', 'max', 'min', 'count'],
    'Age': 'mean'
}).round(2)
print(agg_result)

# Custom aggregation
print("\n\nCustom Aggregation:")
custom_agg = df.groupby('Department')['Salary'].agg(
    average_salary='mean',
    max_salary='max',
    min_salary='min',
    count='count'
).round(2)
print(custom_agg)

# Group by multiple columns
print("\n\nGroup by Multiple Columns:")
# Create a new column for experience level
df['Experience_Level'] = df['Years'].apply(lambda x: 'Senior' if x >= 5 else 'Junior')
grouped = df.groupby(['Department', 'Experience_Level'])['Salary'].mean()
print(grouped)

# ============================================================================
# 7. DATA TRANSFORMATION
# ============================================================================

print("\n\n" + "=" * 70)
print("7. DATA TRANSFORMATION")
print("=" * 70)

# Apply function to column
print("\nApply function to create new column:")
df['Bonus'] = df['Salary'].apply(lambda x: x * 0.1)
print(df[['Name', 'Salary', 'Bonus']])

# Using .apply() on multiple columns
print("\n\nCreate Title from Name:")
df['Title'] = df['Name'].apply(lambda x: 'Mr./Ms. ' + x)
print(df[['Name', 'Title']])

# Categorize salary
print("\n\nSalary Category:")
def categorize_salary(salary):
    if salary >= 80000:
        return 'High'
    elif salary >= 70000:
        return 'Medium'
    else:
        return 'Low'

df['Salary_Category'] = df['Salary'].apply(categorize_salary)
print(df[['Name', 'Salary', 'Salary_Category']])

# ============================================================================
# 8. MERGING DATAFRAMES
# ============================================================================

print("\n\n" + "=" * 70)
print("8. MERGING DATAFRAMES")
print("=" * 70)

# Create two DataFrames
employees = pd.DataFrame({
    'EmployeeID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['IT', 'HR', 'IT', 'Finance']
})

salaries = pd.DataFrame({
    'EmployeeID': [1, 2, 3, 4],
    'Salary': [75000, 60000, 85000, 70000],
    'Bonus': [7500, 3000, 8500, 3500]
})

print("\nEmployees DataFrame:")
print(employees)
print("\nSalaries DataFrame:")
print(salaries)

# Inner join (default)
print("\n\nInner Join (rows present in both):")
merged = pd.merge(employees, salaries, on='EmployeeID')
print(merged)

# Left join
print("\n\nLeft Join (all rows from left DataFrame):")
left_merge = pd.merge(employees, salaries, on='EmployeeID', how='left')
print(left_merge)

# Right join
print("\n\nRight Join (all rows from right DataFrame):")
right_merge = pd.merge(employees, salaries, on='EmployeeID', how='right')
print(right_merge)

# Concatenation (stacking)
print("\n\nConcatenation (Stacking):")
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
concat_result = pd.concat([df1, df2], ignore_index=True)
print(concat_result)

# ============================================================================
# 9. PIVOT TABLES
# ============================================================================

print("\n\n" + "=" * 70)
print("9. PIVOT TABLES")
print("=" * 70)

# Create sample data
sales_data = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=10),
    'Department': ['IT', 'HR', 'IT', 'HR', 'Finance'] * 2,
    'Sales': [10000, 8000, 12000, 7000, 15000, 11000, 9000, 13000, 8500, 14000]
})

print("\nSales Data:")
print(sales_data)

# Create pivot table
print("\n\nPivot Table (Average Sales by Department):")
pivot = sales_data.pivot_table(
    values='Sales',
    index='Department',
    aggfunc='mean'
)
print(pivot)

# ============================================================================
# 10. SORTING AND RANKING
# ============================================================================

print("\n\n" + "=" * 70)
print("10. SORTING AND RANKING")
print("=" * 70)

# Sort by salary (ascending)
print("\nSort by Salary (Ascending):")
sorted_asc = df.sort_values('Salary')
print(sorted_asc[['Name', 'Salary']])

# Sort by salary (descending)
print("\n\nSort by Salary (Descending):")
sorted_desc = df.sort_values('Salary', ascending=False)
print(sorted_desc[['Name', 'Salary']])

# Sort by multiple columns
print("\n\nSort by Department, then Salary:")
sorted_multi = df.sort_values(['Department', 'Salary'], ascending=[True, False])
print(sorted_multi[['Name', 'Department', 'Salary']])

# Ranking
print("\n\nRank Employees by Salary:")
df['Salary_Rank'] = df['Salary'].rank(ascending=False)
print(df[['Name', 'Salary', 'Salary_Rank']])

# ============================================================================
# 11. SAVING AND LOADING DATA
# ============================================================================

print("\n\n" + "=" * 70)
print("11. SAVING AND LOADING DATA")
print("=" * 70)

# Note: These would work if running with file system access
print("\nExamples of saving data:")
print("df.to_csv('employees.csv', index=False)")
print("df.to_excel('employees.xlsx', sheet_name='Employees')")
print("df.to_json('employees.json')")
print("\nExamples of loading data:")
print("df = pd.read_csv('employees.csv')")
print("df = pd.read_excel('employees.xlsx', sheet_name='Employees')")
print("df = pd.read_json('employees.json')")

# ============================================================================
# 12. SUMMARY AND BEST PRACTICES
# ============================================================================

print("\n\n" + "=" * 70)
print("12. KEY PANDAS BEST PRACTICES")
print("=" * 70)

best_practices = """
1. Always check data types with df.info()
2. Use df.describe() to understand numerical data
3. Check for missing values early: df.isnull().sum()
4. Use .query() for readable filtering
5. Use .apply() for transformations, but consider vectorization
6. Always use groupby().agg() with dictionary for clarity
7. Use .copy() when creating filtered DataFrames
8. Sort data consistently for reproducibility
9. Validate data before analysis
10. Save work frequently with to_csv(), to_excel(), etc.
"""

print(best_practices)
