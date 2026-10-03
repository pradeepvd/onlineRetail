import pandas as pd
import numpy as np

file_path = "C://ecommerce-sales-analytics//data//Raw//Online Retail.xlsx"

df =pd.read_excel(file_path)

print(df.head())
print("shape:",df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\ndatatypes:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:")