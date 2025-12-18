CREATE TABLE orders (
    order_id INT,
    order_date DATE,
    customer_id INT,
    status VARCHAR(20)
);

CREATE TABLE order_items (
    order_id INT,
    product_name VARCHAR(100),
    price DECIMAL(10,2),
    quantity INT
);
