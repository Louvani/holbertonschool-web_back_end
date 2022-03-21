-- creates a trigger that decreases the quantity of an item after adding a new order.

CREATE TRIGGER first_trigger
    AFTER INSERT
    ON orders FOR EACH ROW
BEGIN
UPDATE items SET quantity = items.quantity-"orders.number"
    WHERE items.name = "orders.item_name";
END