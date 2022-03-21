-- creates a trigger that decreases the quantity of an item after adding a new order.

CREATE TRIGGER decreases AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
CREATE TRIGGER first_trigger
    AFTER INSERT
    ON orders FOR EACH ROW
BEGIN
UPDATE items SET quantity = items.quantity-"orders.number"
    WHERE items.name = "orders.item_name";
END