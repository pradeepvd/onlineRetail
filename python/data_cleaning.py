import numpy as np
import pandas as pd

df = pd.read_excel("C:\\ecommerce-sales-analytics\\data\\Raw\\Online_Retail.xlsx")
print(df)

print(df.head())
print("shape:",df.shape)
print("\nColumns:",df.columns.to_list())

print("\ndatatypes",df.dtypes)
print("\nInfo:")
print(df.info())

print(df.isnull().sum())

# Display rows with missing descriptions
print(df[df["Description"].isnull()].head())

# Display rows with missing customer IDs
print(df[df["CustomerID"].isnull()].head())

# Count zero unit prices
print("Zero unit prices:", (df["UnitPrice"] == 0).sum())

#count Cancelled orders
print("Cancelled invoices:",df["InvoiceNo"].astype(str).str.startswith("C").sum())

####  make copy of original datasets  ####
sales_df =df.copy()

#Cancelled orders
Cancelled_orders = sales_df[sales_df["InvoiceNo"].astype(str).str.startswith("C")]     #export to csv cancelled

#uncancelled orders
sales_order = sales_df[
    ~sales_df["InvoiceNo"].astype(str).str.startswith("C")]

#Calculates
print("sales_df:",len(sales_df))
print("Cancelled_orders:",len(Cancelled_orders))
print("sales_order:",len(sales_order))

#Revenue of Sales_ordes
sales_order["revenue"] = sales_order["Quantity"] * sales_order["UnitPrice"]
print(sales_order)                                      #salesorder data frame to csv
print(sales_order.columns.to_list())

#Total revenue
Total_revenue = sales_order["revenue"].sum()
print("Total_revenue:",Total_revenue)

#Highest and lowest revenue country
Country_revenue = (sales_order.groupby("Country")["revenue"].sum().sort_values(ascending=False))

print("Highest_country:",Country_revenue.head(1))
print("Lowest_country:",Country_revenue.tail(1))

#cancelled order by country
Cancelled_by_country = Cancelled_orders.groupby("Country")["InvoiceNo"].nunique().sort_values(ascending=False)
print("Cancelled:",Cancelled_by_country)


#Export to csv orderdataframe
try:
    #creating csv
    sales_order.to_csv("Orders_details.csv",index=False)
    print("CSV file created successfully with Pandas!")

except PermissionError as e:
    print("Error: You don’t have permission to write to this location.", e)

except Exception as e:
    print("An unexcepted error occur creating csv file:",e)

### Export cancel order csv
try:
    Cancelled_orders.to_csv("Cancels_order_details.csv",index=False)
    print("cancel order details CSV file created successfully with pandas")

except Exception as e:
    print("An unexpected error occur creating cancel csv file",e)

