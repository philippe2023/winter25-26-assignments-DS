import numpy as np
import pandas as pd

# Part 1:   
# 1. Product Data
product_ids = np.array([1001,1002,1003,1004,1005,1006,1007,1008,1009,1010])

inventory_data = np.array([
    # [stock, avg. weekly sales, price]
    [50,  15.5, 10.99],
    [120,  3.2, 50.50],
    [30,  25.0, 12.99],
    [40,  10.5, 17.99],
    [70,  5.5, 9.99],
    [20,  30.0, 89.99],
    [40,  10.5, 50.50],
    [2,  40.5, 199.99],
    [3,  6.5, 32.50],
    [80,  2.5, 55.0]
])

# 2. Basic Calculations
print(inventory_data.shape)
print(inventory_data.dtype)

# Formula: Total Value = Current Stock Level * Unit Cost
current_stock = inventory_data[:, 0]
price = inventory_data[:, 2]

total_value = current_stock * price
print(total_value)

# 3. Slicing, Indexing, and Statistics
print(inventory_data[3:8])

avg_weekly_sales = np.mean(inventory_data[:, 1])
print(avg_weekly_sales)


cost_of_product = inventory_data[0, 2]
print(cost_of_product)




# Part 2:
# 1. Boolean Masking (The "Low-Stock" Check)

# Weeks of Stock = Current Stock Level / Average Weekly Sales
average_weekly_sales = inventory_data[:, 1]
weeks_of_stock = current_stock / average_weekly_sales
print(weeks_of_stock)


# boolean < than 4
low_stock = weeks_of_stock < 4
print(low_stock)


# low stock products
low_stock_products = inventory_data[low_stock]
print(low_stock_products)


# 2. Reshaping and Concatenation 
# 4 * Average Weekly Sales
reorder_quantity = (4 * average_weekly_sales) - current_stock
print(reorder_quantity)

# ensure negative values become non-negative
reorder_quantity = np.maximum(reorder_quantity, 0)
print(reorder_quantity)

# (10, 1) 2D array
reorder_quantity = reorder_quantity.reshape(10, 1)
print(reorder_quantity)

# concatenate the reorder quantity to the inventory data
reshaped_data = np.concatenate((inventory_data, reorder_quantity), axis=1)
print(reshaped_data)



# Part 3:
# 1. Dataframe Creation
df = pd.DataFrame(reshaped_data, columns=['Stock', 'Average Weekly Sales', 'Price', 'Reorder Quantity'])
print(df)

# 2. Basic Selection
basic_selection_df = df[['Stock', 'Reorder Quantity']]
print(basic_selection_df)

first_5_rows = df.head(5)
print(first_5_rows)











