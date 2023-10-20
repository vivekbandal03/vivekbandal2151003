import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data (replace this with your actual sales data)
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Hour': [9, 10, 11, 12, 13],
    'Product': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B'],
    'Quantity': [10, 15, 8, 12, 9]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to a datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Analyze sales trends over time
daily_sales = df.groupby('Date')['Quantity'].sum()
hourly_sales = df.groupby('Hour')['Quantity'].sum()

# Create data visualizations
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
daily_sales.plot(kind='line')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')

plt.subplot(1, 2, 2)
hourly_sales.plot(kind='bar')
plt.title('Hourly Sales')
plt.xlabel('Hour')
plt.ylabel('Total Sales')

plt.tight_layout()
plt.show()

# Identify peak sales hours and popular products
peak_hour = hourly_sales.idxmax()
popular_product = df['Product'].mode()[0]

print(f"Peak Sales Hour: {peak_hour} o'clock")
print(f"Popular Product: {popular_product}")

# Generate reports for store management
print("Daily Sales Report:")
print(daily_sales)

print("Hourly Sales Report:")
print(hourly_sales)
