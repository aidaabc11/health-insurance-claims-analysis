# 1_data_inspection.ipynb

import pandas as pd

# Load data
df = pd.read_csv('../data/insurance.csv')

# Preview
print("🔹 Top 5 rows")
display(df.head())

print("\n🔹 Dataset Info")
df.info()

print("\n🔹 Descriptive Stats")
display(df.describe())

print("\n🔹 Missing values:")
display(df.isnull().sum())
