-- 6. Add bonus
DELIMITER $$
CREATE PROCEDURE addBonus(
	IN user_id INT, project_name varchar(255), score INT
)
BEGIN
	UPDATE corrections SET NEW.user_id = user_id, NEW.score = score
END;
//
