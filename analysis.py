import pandas as pd

data = pd.read_csv("sales_data.csv")

data['date'] = pd.to_datetime(data['date'])
data['month'] = data['date'].dt.month

print(data.head())

# Total sales
print("Total Sales:", data['sales'].sum())

# Monthly sales
print(data.groupby('month')['sales'].sum())

# Top products
print(data.groupby('product')['sales'].sum().sort_values(ascending=False))

# Region performance
print(data.groupby('region')['sales'].sum())

import matplotlib.pyplot as plt

# Monthly sales
data.groupby('month')['sales'].sum().plot(kind='line')
plt.title("Monthly Sales")
plt.show()

# Region sales
data.groupby('region')['sales'].sum().plot(kind='bar')
plt.title("Region Sales")
plt.show()