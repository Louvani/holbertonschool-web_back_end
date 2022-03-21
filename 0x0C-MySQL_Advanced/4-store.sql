-- creates a trigger that decreases the quantity of an item after adding a new order.

CREATE TRIGGER first_trigger
    AFTER INSERT
    ON orders FOR EACH ROW
BEGIN
UPDATE items SET quantity = items.quantity-NEW.number
    WHERE items.name = NEW.item_name;
END