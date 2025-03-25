# 📊 SQL Retail Sales Analysis

## 📌 Overview
This project contains SQL queries for analyzing retail sales data. It includes data cleaning, exploration, and key business insights.

## 🗄️ Database & Table Setup
### **1️⃣ Create Database**
```sql
CREATE DATABASE Rental_sales_analysis;
```

### **2️⃣ Create Table**
```sql
DROP TABLE IF EXISTS Retail_Sales; -- Drop table if already exists

CREATE TABLE Retail_Sales (
    transaction_id INT PRIMARY KEY,
    sale_date DATE,
    sale_time TIME,
    customer_id INT,
    gender VARCHAR(15),
    age INT,
    category VARCHAR(15),
    quantity INT,
    price_per_unit FLOAT,
    cogs FLOAT, -- Cost of Goods Sold
    total_sale FLOAT
);
```

### **3️⃣ View Sample Data**
```sql
SELECT * FROM Retail_Sales LIMIT 20;
```

## 🔍 Data Cleaning
### **Check for NULL values**
```sql
SELECT * FROM Retail_Sales
WHERE transaction_id IS NULL
   OR sale_date IS NULL
   OR sale_time IS NULL
   OR gender IS NULL
   OR category IS NULL
   OR quantity IS NULL
   OR cogs IS NULL
   OR total_sale IS NULL;
```

### **Remove NULL values**
```sql
DELETE FROM Retail_Sales
WHERE transaction_id IS NULL
   OR sale_date IS NULL
   OR sale_time IS NULL
   OR gender IS NULL
   OR category IS NULL
   OR quantity IS NULL
   OR cogs IS NULL
   OR total_sale IS NULL;
```

## 📊 Data Exploration & Business Insights
### **1️⃣ How many unique customers?**
```sql
SELECT COUNT(DISTINCT customer_id) AS total_customers FROM Retail_Sales;
```

### **2️⃣ How many customers made repeat purchases?**
```sql
SELECT COUNT(customer_id) AS repeated_customers
FROM (
    SELECT customer_id
    FROM Retail_Sales
    GROUP BY customer_id
    HAVING COUNT(customer_id) > 1
) AS repeated;
```

### **3️⃣ Gender distribution of customers**
```sql
SELECT gender, COUNT(DISTINCT customer_id) AS total_customers
FROM Retail_Sales
GROUP BY gender;
```

### **4️⃣ Average age of customers**
```sql
SELECT AVG(age) AS avg_age FROM Retail_Sales;
```

### **5️⃣ Total revenue generated**
```sql
SELECT SUM(total_sale) AS total_revenue FROM Retail_Sales;
```

### **6️⃣ Highest sale in a single transaction**
```sql
SELECT MAX(total_sale) AS highest_sale FROM Retail_Sales;
```

### **7️⃣ Date with highest total sales**
```sql
SELECT sale_date, SUM(total_sale) AS total_revenue
FROM Retail_Sales
GROUP BY sale_date
ORDER BY total_revenue DESC
LIMIT 1;
```

### **8️⃣ Average revenue per transaction**
```sql
SELECT AVG(total_sale) AS avg_transaction_value FROM Retail_Sales;
```

### **9️⃣ Top revenue-generating category**
```sql
SELECT category, SUM(total_sale) AS total_revenue
FROM Retail_Sales
GROUP BY category
ORDER BY total_revenue DESC
LIMIT 1;
```

### **🔟 Most frequently purchased category**
```sql
SELECT category, COUNT(*) AS total_purchases
FROM Retail_Sales
GROUP BY category
ORDER BY total_purchases DESC
LIMIT 1;
```

### **1️⃣1️⃣ Average quantity per purchase**
```sql
SELECT AVG(quantity) AS avg_quantity FROM Retail_Sales;
```

### **1️⃣2️⃣ Hour of the day with highest sales**
```sql
SELECT EXTRACT(HOUR FROM sale_time) AS sale_hour, COUNT(*) AS total_sales
FROM Retail_Sales
GROUP BY sale_hour
ORDER BY total_sales DESC
LIMIT 1;
```

### **1️⃣3️⃣ Total sales per day of the week**
```sql
SELECT TO_CHAR(sale_date, 'Day') AS day_of_week, SUM(total_sale) AS total_sales
FROM Retail_Sales
GROUP BY day_of_week
ORDER BY total_sales DESC;
```

### **1️⃣4️⃣ Month with highest revenue**
```sql
SELECT TO_CHAR(sale_date, 'Month') AS month, SUM(total_sale) AS total_revenue
FROM Retail_Sales
GROUP BY month
ORDER BY total_revenue DESC
LIMIT 1;
```

### **1️⃣5️⃣ Total Cost of Goods Sold (COGS)**
```sql
SELECT SUM(cogs) AS total_cogs FROM Retail_Sales;
```

### **1️⃣6️⃣ Total profit generated**
```sql
SELECT SUM(total_sale - cogs) AS total_profit FROM Retail_Sales;
```

### **1️⃣7️⃣ Profit margin percentage**
```sql
SELECT (SUM(total_sale - cogs) / SUM(total_sale)) * 100 AS profit_margin_percentage
FROM Retail_Sales;
```

## 🎯 Conclusion
This SQL script provides deep insights into retail sales, covering:
- Customer trends
- Revenue analysis
- Peak sales periods
- Profitability metrics

🚀 **Use these queries to optimize business decisions and drive data-driven growth!** 🚀


