# Write your MySQL query statement below
SELECT u.product_id, 
       ROUND(SUM(u.units * p.price) / SUM(u.units), 2) AS average_price
FROM UnitsSold u
JOIN Prices p 
ON u.product_id = p.product_id 
AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY u.product_id

UNION 

SELECT product_id, 0 AS average_price
FROM Prices 
WHERE product_id NOT IN (SELECT DISTINCT product_id FROM UnitsSold);