SELECT products.product_name AS 'Товар', count(products.product_name) AS 'Количество заказов' FROM orders
JOIN products ON orders.id_product=products.id_product
GROUP BY orders.id_product
ORDER BY product_name;