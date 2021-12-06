-- 1 вариант
SELECT user_name AS 'Клиент', rnd AS 'Общая сумма покупок' FROM clients
JOIN 
(SELECT ROUND(SUM(price), 2) AS rnd, id_users FROM products
JOIN orders
ON products.id_product=orders.id_product
GROUP BY id_users) AS price_sum
ON clients.id_users=price_sum.id_users
ORDER BY user_name;
-- 2 вариант
/*
SELECT user_name AS 'Клиент', rnd AS 'Общая сумма покупок' FROM clients
JOIN 
(SELECT ROUND(SUM(price), 2) AS rnd, id_users FROM products
JOIN
(SELECT id_users, id_product FROM orders) AS ord
ON products.id_product=ord.id_product
GROUP BY id_users) AS price_sum
ON clients.id_users=price_sum.id_users
ORDER BY user_name;
*/