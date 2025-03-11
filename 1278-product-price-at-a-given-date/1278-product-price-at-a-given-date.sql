SELECT product_id, new_price AS price
FROM products
WHERE (product_id, change_date) IN
(   
    SELECT product_id, MAX(change_date)
    FROM products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)
UNION
SELECT product_id, 10 AS price
FROM products p
WHERE NOT EXISTS 
(
    SELECT 1 
    FROM products p2
    WHERE p.product_id = p2.product_id
    AND change_date <= '2019-08-16'
);
