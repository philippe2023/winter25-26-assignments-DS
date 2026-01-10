"Assignment 3: Global Sales Data Analyst"

import numpy as np
import pandas as pd

# PART 1: Reading and Inspecting Data

print("=" * 60)
print("PART 1: READING AND INSPECTING DATA")
print("=" * 60)

# Read the data
df = pd.read_csv('global_sales.csv')

# Print the first 5 rows and the data types of all columns
print("\nFirst 5 rows:")
print(df.head())

print("\nData types of all columns:")
print(df.dtypes)


# PART 2: Data Cleaning and Indexing

# Part 2.1: Handling Missing Values and Casting
missing_values = df.isnull().sum()
print(missing_values)

# Replace missing values with 0
df = df.fillna(0)

# Fill Missing Values in Units_Sold column with the mean value
df["Units_Sold"] = pd.to_numeric(df["Units_Sold"], errors="coerce")
units_sold_mean = df["Units_Sold"].mean()
df["Units_Sold"] = df["Units_Sold"].fillna(units_sold_mean)

print("Units_Sold after filling missing values:")
print(df["Units_Sold"].describe())

# Data Type Casting: 
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Sales"] = df["Sales"].fillna(0).astype(float)

print("Sales after cleaning:")
print(df["Sales"].describe())

# Casting Dates: Convert Date column to datetime 
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

invalid_date_count = df["Date"].isna().sum()
if invalid_date_count > 0:
    print(f"Warning: {invalid_date_count} rows have invalid dates.")

print("\nDate column info:")
print(df["Date"].head())

print("\nData types after cleaning:")
print(df.dtypes)


# Part 2.2: Indexing and Setting

# Use the OrderID column to set a new index for the DataFrame
df = df.set_index("OrderID")

print("DataFrame with OrderID as index:")
print(df.head())
print("Index name:", df.index.name)

# Reset the index, and then set the Date column as the index
df = df.reset_index()
df = df.set_index("Date")

print("setting Date as index:")
print(df.head())
print("Index name:", df.index.name)


# PART 3: Filtering, Modifying, and Sorting

# Part 3.1: Filtering Data
print("\nCheck Sales column type:", df["Sales"].dtype)
print("Unique regions:", df["Region"].unique())

high_value_sales = df[(df["Sales"] > 500) & (df["Region"] == "Europe")]
print(high_value_sales)
print("\nNumber of rows in high_value_sales:", len(high_value_sales))


# Part 3.2: Updating and Adding Columns

# Update a Row: Select a specific row (5th row)
print("\nChecking before update (5th row):")
print(df.iloc[4])

df.iloc[4, df.columns.get_loc("Units_Sold")] = 99

print("\nAfter update (5th row):")
print(df.iloc[4])

# Add Profit column (20% of Sales)
df["Profit"] = df["Sales"] * 0.20

print("\nProfit column added. Quick check:")
print(df[["Sales", "Profit"]].head())


# Part 3.3: Sorting Data
sorted_df = df.sort_values(by=["Region", "Sales"], ascending=[True, False])
print("\nSorted by Region (ascending) and Sales (descending):")
print(sorted_df)


# PART 4: Grouping and Aggregation (Analysis)

# Part 4.1: Regional Performance
regional_summary = df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Avg_Units_Sold=("Units_Sold", "mean")
)

print("\nRegional Performance (Total Sales + Avg Units Sold):")
print(regional_summary)

# Part 4.2: Product Deep Dive
max_profit_by_product = df.groupby("Product")["Profit"].max()
print("\nMax Profit by Product:")
print(max_profit_by_product)


# Part 4.3: Time Series Analysis
monthly_sales = df["Sales"].resample("ME").sum()
print("\nMonthly Total Sales:")
print(monthly_sales)


