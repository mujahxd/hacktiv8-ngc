DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name TEXT NOT NULL,
    city TEXT NOT NULL
);

INSERT INTO Customers (customer_name, city) VALUES
    ('John Doe', 'New York'),
    ('Jane Smith', 'Los Angeles'),
    ('David Johnson', 'Chicago');

DROP TABLE IF EXISTS Orders;

CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
    total_amount NUMERIC(10, 2) NOT NULL
);

INSERT INTO Orders (customer_id, order_date, total_amount) VALUES 
	(1, '2022-01-10', 100.00),
	(1, '2022-02-15', 150.00),
	(2, '2022-03-20', 200.00),
	(3, '2022-04-25', 50.00);
	
SELECT c.customer_name, COUNT(*) AS total_orders
FROM Customers c
JOIN Orders o USING (customer_id)
GROUP BY c.customer_name
ORDER BY total_orders DESC, c.customer_name DESC;