import numpy as np
import matplotlib.pyplot as plt

# Sample Data
np.random.seed(0)
dates = np.arange('2023-01', '2024-01', dtype='datetime64[M]')
sales_revenue = np.random.randint(1000, 5000, size=len(dates))
product_quantities = np.random.randint(200, 800, size=len(dates))
customer_demographics = np.random.choice(['Youth', 'Adult', 'Senior'], size=len(dates))

# Sales Revenue over Time (Line Plot)
plt.figure(figsize=(14, 8))
plt.subplot(2, 2, 1)
plt.plot(dates, sales_revenue, label='Sales Revenue', color='blue')
plt.fill_between(dates, sales_revenue, alpha=0.2, color='blue')
plt.title('Sales Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.legend()
plt.grid(True)

# Product Quantities Sold over Time (Area Chart)
plt.subplot(2, 2, 2)
plt.fill_between(dates, product_quantities, color='green', alpha=0.6)
plt.plot(dates, product_quantities, color='green', alpha=0.9, label='Quantities Sold')
plt.title('Product Quantities Sold Over Time')
plt.xlabel('Date')
plt.ylabel('Quantity')
plt.legend()
plt.grid(True)

# Sales Performance Comparison across Categories (Bar Plot)
categories = ['Electronics', 'Clothing', 'Home Goods', 'Books']
sales_by_category = np.random.randint(5000, 20000, size=len(categories))
plt.subplot(2, 2, 3)
plt.bar(categories, sales_by_category, color=['purple', 'orange', 'cyan', 'red'])
plt.title('Sales Performance by Category')
plt.xlabel('Product Category')
plt.ylabel('Sales ($)')
plt.grid(True)

# Distribution of Sales by Customer Segment (Pie Chart)
segments, counts = np.unique(customer_demographics, return_counts=True)
plt.subplot(2, 2, 4)
plt.pie(counts, labels=segments, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightblue', 'lightcoral'])
plt.title('Sales Distribution by Customer Segment')

# Adjust layout and show the dashboard
plt.tight_layout()
plt.show()
