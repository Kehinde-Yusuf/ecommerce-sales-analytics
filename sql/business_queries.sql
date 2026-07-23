-- ====================================================================================
--QUESTION 1
--TOTAL REVENUE
-- ====================================================================================
SELECT SUM(amount_paid) as Total_Revenue
FROM orders
-- ====================================================================================
--QUESTION 2
--AVERAGE AMOUNT PER ORDER
-- ====================================================================================
SELECT AVG(amount_paid) AS average_amount
FROM orders
-- ====================================================================================
--QUESTION 3
--HIGHEST AND LOWEST AMOUNT PAID FOR A SINGLE ORDER
-- ====================================================================================
SELECT MAX(amount_paid) AS highest_amount_paid,
       MIN(amount_paid) AS lowest_amount_paid
FROM orders;
-- ====================================================================================
--QUESTION 4
--5 CUSTOMERS WHO SPENT THE MOST MONEY
-- ====================================================================================
SELECT o.customer_id, c.name, SUM(o.amount_paid) AS total_money_spent
FROM customers as c
JOIN orders as o
ON c.id = o.customer_id
Where o.amount_paid IS NOT NULL
GROUP BY o.customer_id, name
ORDER BY total_money_spent desc
LIMIT 5;
-- ===================================================================================
--QUESTION 5
--TOP 5 MOST PURCHASED PRODUCTS
-- ===================================================================================
SELECT p.product_id, p.product_name, SUM(o.quantity_purchased) AS most_purchased
FROM products AS p
JOIN orders AS o
ON p.product_id = o.product_id
GROUP BY p.product_id, p.product_name
ORDER BY most_purchased DESC
LIMIT 5
-- ===================================================================================
--QUESTION 6 
--TOTAL REVENUE BY EACH PRODUCT CATEGORY
-- ===================================================================================
SELECT p.category, SUM(o.amount_paid) AS total_revenue
FROM products AS p
JOIN orders AS o
ON p.product_id = o.product_id
GROUP BY p.category
ORDER BY total_revenue desc
-- ====================================================================================
--QUESTION 7
--THE MOST PURCHASED ITEMS PER MONTH FOR EACH YEAR
-- ====================================================================================
SELECT *
FROM (
SELECT p.product_name, 
       EXTRACT(YEAR FROM o.order_date) AS year,
	   EXTRACT(MONTH FROM o.order_date) AS month,
	   SUM(o.quantity_purchased) AS total_quantity,

	   ROW_NUMBER() OVER (
	       PARTITION BY
		       EXTRACT(YEAR FROM o.order_date),
			   EXTRACT(MONTH FROM o.order_date)
		   ORDER BY
		       SUM(o.quantity_purchased)DESC
	   ) AS rn
	   
FROM products AS p
JOIN orders AS o
ON p.product_id = o.product_id
GROUP BY p.product_name, 
         EXTRACT(YEAR FROM o.order_date), 
	     EXTRACT(MONTH FROM o.order_date)
) AS ranked_products
WHERE rn = 1

ORDER BY year, month;
-- ======================================================================================
--QUESTION 8
--PROFIT AND PROFIT PERCENTAGE
-- ======================================================================================
SELECT
    SUM(o.amount_paid) AS total_revenue,
	SUM(p.cost_price * o.quantity_purchased) AS total_cost,
	SUM(o.amount_paid - (p.cost_price * o.quantity_purchased))AS total_profit,

  ROUND(
      (
	      SUM(o.amount_paid - (p.cost_price * o.quantity_purchased))
		  /
		  SUM(o.amount_paid)
	  ) * 100,
	  2
   ) AS profit_percentage
FROM orders o
JOIN products p
ON o.product_id = p.product_id;
-- ====================================================================================
--QUESTION 9
--MONTHLY REVENUE TREND
-- ====================================================================================
SELECT 
      EXTRACT(YEAR FROM order_date) AS year,
	  EXTRACT(MONTH FROM order_date) AS month,
	  SUM(amount_paid) AS total_revenue
FROM orders 
GROUP BY
    EXTRACT(YEAR FROM order_date),
    EXTRACT(MONTH FROM order_date) 
ORDER BY
    year,
	month;
