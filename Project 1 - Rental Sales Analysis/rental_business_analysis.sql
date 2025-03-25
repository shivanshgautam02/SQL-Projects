-- SQL Retail Sales Analysis - P1
CREATE DATABASE Rental_sales_analysis;


-- Create TABLE
DROP TABLE IF EXISTS Retail_Sales; -- This will drop any pre existing table with same name


CREATE TABLE Retail_Sales
            (
                transaction_id INT PRIMARY KEY,	
                sale_date DATE,	 
                sale_time TIME,	
                customer_id	INT,
                gender	VARCHAR(15),
                age	INT,
                category VARCHAR(15),	
                quantity	INT,
                price_per_unit FLOAT,	
                cogs	FLOAT,                               -- Cost of Goods Sold
                total_sale FLOAT
            );

SELECT * FROM Retail_Sales
LIMIT 20;									-- Applying limit to see only first 20 rows of data


    
-- Total rows in database

SELECT COUNT(*) 
FROM Retail_Sales;


-- Data Cleaning

SELECT * FROM Retail_Sales							-- To view null values in a cloumn
WHERE transaction_id IS NULL;


SELECT * FROM Retail_Sales
WHERE 
    transaction_id IS NULL
    OR
    sale_date IS NULL
    OR 
    sale_time IS NULL
    OR
    gender IS NULL
    OR
    category IS NULL
    OR
    quantity IS NULL
    OR
    cogs IS NULL
    OR
    total_sale IS NULL;


   
-- Deleting  NUll entites of data

DELETE FROM Retail_Sales
WHERE 
    transaction_id IS NULL
    OR
    sale_date IS NULL
    OR 
    sale_time IS NULL
    OR
    gender IS NULL
    OR
    category IS NULL
    OR
    quantity IS NULL
    OR
    cogs IS NULL
    OR
    total_sale IS NULL;


	
-- Data Exploration

-- How many sales we have?
SELECT COUNT(*) as total_sale 
FROM Retail_Sales;


-- How many uniuque customers we have ?

SELECT COUNT(DISTINCT customer_id) as total_sale FROM Retail_Sales;

-- The number of customers who have made more than one purchase 

SELECT COUNT(customer_id) AS repeated_customers
FROM (
    SELECT customer_id
    FROM Retail_Sales
    GROUP BY customer_id
    HAVING COUNT(customer_id) > 1
) AS repeated;


SELECT DISTINCT category FROM Retail_Sales;


-- Data Analysis & Business Key Problems & Answers

-- My Analysis & Findings
-- 1. How many unique customers do we have?
-- 2. How many customers have made repeat purchases?
-- 3. What is the gender distribution of customers?
-- 4. What is the average age of customers?
-- 5. What is the total revenue generated?
-- 6. What is the highest sale amount recorded in a single transaction?
-- 7. Which date had the highest total sales?
-- 8. What is the average revenue per transaction?
-- 9. Which product category generates the highest revenue?
-- 10. What is the most frequently purchased product category?
-- 11. What is the average quantity per purchase?
-- 12. Which hour of the day has the highest number of sales?
-- 13. What are the total sales per day of the week?
-- 14. Which month has the highest revenue?
-- 15. What is the total Cost of Goods Sold (COGS)?
-- 16. What is the total profit generated?
-- 17. What is the profit margin percentage?


--

-- 1. Customer Insights

-- 1. How many unique customers do we have?  


SELECT COUNT(DISTINCT customer_id) AS total_customers FROM Retail_Sales;
   

-- 2. How many customers have made repeat purchases?  

SELECT COUNT(customer_id) AS repeated_customers
   FROM (
       SELECT customer_id
       FROM Retail_Sales
       GROUP BY customer_id
       HAVING COUNT(customer_id) > 1
   ) AS repeated;


-- 3. What is the gender distribution of customers?  
   
SELECT gender, COUNT(DISTINCT customer_id) AS total_customers
   FROM Retail_Sales
   GROUP BY gender;
   

-- 4. What is the average age of customers?  
   
SELECT AVG(age) AS avg_age FROM Retail_Sales;
   
  
-- 5. What is the total revenue generated?  
   
SELECT SUM(total_sale) AS total_revenue FROM Retail_Sales;
   

-- 6. What is the highest sale amount recorded in a single transaction?  
   
SELECT MAX(total_sale) AS highest_sale FROM Retail_Sales;
   

-- 7. Which date had the highest total sales?  

SELECT sale_date, SUM(total_sale) AS total_revenue
   FROM Retail_Sales
   	GROUP BY sale_date
   	ORDER BY total_revenue DESC
   	LIMIT 1;

-- 8. What is the average revenue per transaction?  

SELECT AVG(total_sale) AS avg_transaction_value FROM Retail_Sales;


  
-- 9. Which product category generates the highest revenue?  

SELECT category, SUM(total_sale) AS total_revenue
   FROM Retail_Sales
   	GROUP BY category
   	ORDER BY total_revenue DESC
   	LIMIT 1;


-- 10. What is the most frequently purchased product category?  

SELECT category, COUNT(*) AS total_purchases
   FROM Retail_Sales
 	   GROUP BY category
	   ORDER BY total_purchases DESC
   	   LIMIT 1;


-- 11. What is the average quantity per purchase?  
   
SELECT AVG(quantity) AS avg_quantity FROM Retail_Sales;

  
-- 12. Which hour of the day has the highest number of sales?  

SELECT EXTRACT(HOUR FROM sale_time) AS sale_hour, COUNT(*) AS total_sales
	FROM Retail_Sales
		GROUP BY sale_hour
		ORDER BY total_sales DESC
		LIMIT 1;


-- 13. What are the total sales per day of the week?  
   
SELECT DAYNAME(sale_date) AS day_of_week, SUM(total_sale) AS total_sales
	FROM Retail_Sales
		GROUP BY day_of_week
		ORDER BY total_sales DESC;
   

--  14. Which month has the highest revenue?  

SELECT TO_CHAR(sale_date, 'Month') AS month, SUM(total_sale) AS total_revenue
	FROM Retail_Sales
		GROUP BY month
		ORDER BY total_revenue DESC
		LIMIT 1;



-- 15. What is the total Cost of Goods Sold (COGS)?  

SELECT SUM(cogs) AS total_cogs FROM Retail_Sales;


-- 16. What is the total profit generated?  

SELECT SUM(total_sale - cogs) AS total_profit FROM Retail_Sales;

-- 17. What is the profit margin percentage?  

SELECT 
    (SUM(total_sale - cogs) / SUM(total_sale)) * 100 AS profit_margin_percentage
FROM Retail_Sales;

-- THE END