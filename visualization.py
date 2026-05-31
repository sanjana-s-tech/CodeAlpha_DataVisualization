import pandas as pd
import matplotlib.pyplot as plt
import os

# Create charts folder
if not os.path.exists("charts"):
    os.makedirs("charts")

df = pd.read_excel(r"C:\Users\s sanjana\Downloads\Financial Sample.xlsx")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("Columns:")
print(df.columns.tolist())

# -------------------------
# Sales by Country
# -------------------------
country_sales = df.groupby("Country")["Sales"].sum()

plt.figure(figsize=(10,5))
country_sales.sort_values(ascending=False).plot(kind="bar")
plt.title("Total Sales by Country")
plt.xlabel("Country")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("charts/sales_by_country.png")
plt.show()

# -------------------------
# Profit by Product
# -------------------------
product_profit = df.groupby("Product")["Profit"].sum()

plt.figure(figsize=(10,5))
product_profit.sort_values(ascending=False).plot(kind="bar")
plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("charts/profit_by_product.png")
plt.show()

# -------------------------
# Sales by Segment
# -------------------------
segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(8,8))
segment_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.ylabel("")
plt.title("Sales Distribution by Segment")
plt.tight_layout()
plt.savefig("charts/sales_by_segment.png")
plt.show()

# -------------------------
# Monthly Sales Trend
# -------------------------
df["Date"] = pd.to_datetime(df["Date"])

monthly_sales = df.groupby("Month Name")["Sales"].sum()

monthly_sales = monthly_sales.reindex([
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
])

plt.figure(figsize=(10,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/monthly_sales_trend.png")
plt.show()

# -------------------------
# Profit by Country
# -------------------------
country_profit = df.groupby("Country")["Profit"].sum()

plt.figure(figsize=(10,5))
country_profit.sort_values(ascending=False).plot(kind="bar")
plt.title("Profit by Country")
plt.xlabel("Country")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("charts/profit_by_country.png")
plt.show()

# -------------------------
# Top 10 Products by Sales
# -------------------------
top_products = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Product Sales Comparison")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("charts/product_sales_comparison.png")
plt.show()

# -------------------------
# Insights
# -------------------------
print("\nKEY INSIGHTS")
print("Highest Sales Country:", country_sales.idxmax())
print("Highest Profit Product:", product_profit.idxmax())
print("Highest Profit Country:", country_profit.idxmax())

print("\nCharts saved successfully in charts folder.")