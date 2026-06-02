import pandas as pd

df = pd.read_csv("Dataset/Dataset.csv")

print("Rows and Columns:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nAggregate Rating Statistics:")
print(df["Aggregate rating"].describe())