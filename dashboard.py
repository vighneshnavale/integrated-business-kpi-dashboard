
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read Excel data
df = pd.read_excel("sales_data.xlsx")

# Step 2: Calculate sales, cost and profit
df["Sales"] = df["Quantity"] * df["Unit_Price"]
df["Cost"] = df["Quantity"] * df["Cost_Per_Unit"]
df["Profit"] = df["Sales"] - df["Cost"]

# Step 3: Calculate KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
average_sales = df["Sales"].mean()

profit_percentage = 0
if total_sales > 0:
    profit_percentage = total_profit / total_sales * 100

# Step 4: Display results
print("BUSINESS KPI DASHBOARD")
print("----------------------")
print("Total Sales: Rs.", total_sales)
print("Total Profit: Rs.", total_profit)
print("Total Quantity:", total_quantity)
print("Average Sales: Rs.", round(average_sales, 2))
print("Profit Percentage:", round(profit_percentage, 2), "%")

# Step 5: Prepare monthly sales data
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month
monthly_sales = df.groupby("Month")["Sales"].sum()

# Step 6: Prepare category data
category_sales = df.groupby("Category")["Sales"].sum()
category_profit = df.groupby("Category")["Profit"].sum()

# Step 7: Create dashboard
fig, ax = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Integrated Business Data Analysis and KPI Dashboard",
             fontsize=15, fontweight="bold")

# Show KPIs
fig.text(0.5, 0.90,
         f"Sales: Rs. {total_sales:,.0f}  |  "
         f"Profit: Rs. {total_profit:,.0f}  |  "
         f"Quantity: {total_quantity}  |  "
         f"Profit %: {profit_percentage:.2f}%",
         ha="center", fontsize=10)

# Chart 1: Monthly Sales
ax[0, 0].bar(monthly_sales.index, monthly_sales.values)
ax[0, 0].set_title("Monthly Sales")
ax[0, 0].set_xlabel("Month Number")
ax[0, 0].set_ylabel("Sales (Rs.)")

# Chart 2: Sales by Category
ax[0, 1].pie(category_sales.values,
             labels=category_sales.index,
             autopct="%1.1f%%")
ax[0, 1].set_title("Sales by Category")

# Chart 3: Profit by Category
ax[1, 0].bar(category_profit.index, category_profit.values)
ax[1, 0].set_title("Profit by Category")
ax[1, 0].set_xlabel("Category")
ax[1, 0].set_ylabel("Profit (Rs.)")

# Chart 4: Sales vs Profit
ax[1, 1].bar(["Sales", "Profit"],
             [total_sales, total_profit])
ax[1, 1].set_title("Sales vs Profit")
ax[1, 1].set_ylabel("Amount (Rs.)")

# Step 8: Show and save dashboard
plt.tight_layout(rect=[0, 0, 1, 0.85])
plt.savefig("kpi_dashboard.png", dpi=300)   
plt.show()
