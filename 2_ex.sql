SELECT user_name 'Клиент' FROM clients
JOIN 
(SELECT id_users, product_name FROM orders
JOIN products ON orders.id_product=products.id_product
WHERE product_name='Телефон') AS u_lst
ON clients.id_users=u_lst.id_users 
ORDER BY user_name;