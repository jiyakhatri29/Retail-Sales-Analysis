import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

try:

  df=pd.read_csv("retail_sales.csv")
  print(df.describe())

# print(df.head())

  print("Null values count is exist: \n", df.isnull().sum())

#filling missing/null values if occur
  df["Units_Sold"]=df["Units_Sold"].fillna(df["Units_Sold"].mean())  
  df["Price_Per_Unit"]=df["Price_Per_Unit"].fillna(df["Price_Per_Unit"].mean())

  df["Profit"]=df["Profit"].fillna(df["Profit"].mean())

# print(df.head())
  df=df.drop_duplicates()
  df["Order_Date"]=pd.to_datetime(df["Order_Date"])
# after data cleaning now we can add or remove columns so created a new column.

  df["Total_sales"]=df["Units_Sold"]*df["Price_Per_Unit"]

  df["Profit_Margin"] = (df["Profit"] / df["Total_sales"]) * 100

  print(df.head())
# print(type("Order_Data"))

  df["Sales_category"]=np.where(df["Total_sales"]>50000,"High Sales", "Low Sales")
  print(df.head(10))

  region_sales=df.groupby("Region")["Total_sales"].sum()
  print(region_sales)

  Product_sales=df.groupby("Product")["Total_sales"].sum()
  print(Product_sales)

  Category_sales=df.groupby("Category")["Total_sales"].sum()
  print(Category_sales)


  top_sales=df.sort_values("Total_sales", ascending=False)

  print(top_sales.head())


  avg_sales = np.mean(df["Total_sales"])
  max_sales = np.max(df["Total_sales"])
  min_sales = np.min(df["Total_sales"])

  print("\n===== NUMPY ANALYSIS =====")

  print("Average Sales:", avg_sales)
  print("Maximum Sales:", max_sales)
  print("Minimum Sales:", min_sales)

  df["Month"] = df["Order_Date"].dt.month_name()

  monthly_sales = df.groupby("Month")["Total_sales"].sum()

  print("\n===== MONTHLY SALES =====")


  print(monthly_sales)


#Adding Matplotlib
#Region-wise Sales (Bar Chart)

  plt.figure(figsize=(8,5))
  region_sales.plot(kind="bar")
  plt.title("Region-wise Total Sales")
  plt.xlabel("Region")
  plt.ylabel("Total Sales")
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()

# Product-wise Sales (Horizontal Bar Chart)
  plt.figure(figsize=(8,6))
  Product_sales.plot(kind="barh")
  plt.title("Product-wise Sales")
  plt.xlabel("Total Sales")
  plt.ylabel("Product")
  plt.tight_layout()
  plt.show()

#Category-wise Sales (Pie Chart)
  plt.figure(figsize=(7,7))
  Category_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
  )
  plt.title("Category-wise Sales Distribution")
  plt.ylabel("")
  plt.show()

#Monthly Sales Trend (Line Chart)

  plt.figure(figsize=(10,5))
  monthly_sales.plot(marker="o", linewidth=2)
  plt.title("Monthly Sales Trend")
  plt.xlabel("Month")
  plt.ylabel("Total Sales")
  plt.xticks(rotation=45)
  plt.grid(True)
  plt.tight_layout()
  plt.show()

#Profit Distribution (Histogram)

  plt.figure(figsize=(8,5))
  plt.hist(df["Profit"], bins=10)
  plt.title("Profit Distribution")
  plt.xlabel("Profit")
  plt.ylabel("Frequency")
  plt.tight_layout()
  plt.show()

# Units Sold vs Total Sales (Scatter Plot)


  plt.figure(figsize=(8,5))
  plt.scatter(df["Units_Sold"], df["Total_sales"])
  plt.title("Units Sold vs Total Sales")
  plt.xlabel("Units Sold")
  plt.ylabel("Total Sales")
  plt.tight_layout()
  plt.show()

#High Sales vs Low Sales Count
  sales_count = df["Sales_category"].value_counts()

  plt.figure(figsize=(6,5))
  sales_count.plot(kind="bar")
  plt.title("Sales Category")
  plt.xlabel("Category")
  plt.ylabel("Count")
  plt.tight_layout()
  plt.show()




  df.to_csv("final_sales_report.csv", index=False)

  print("\nProject completed successfully!")
  print("Data cleaned successfully.")
  print("Analysis completed.")
  print("Visualizations generated.")
  print("Final report saved as final_sales_report.csv")
  
except FileNotFoundError:
    print("Error: retail_sales.csv file not found.")

except KeyError as e:
    print(f"Error: Column {e} not found in the dataset.")

except Exception as e:
    print("Unexpected Error:", e)