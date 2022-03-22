-- 6. Add bonus
DELIMITER //
CREATE PROCEDURE AddBonus(
	IN user_id INT, project_name varchar(255), score INT
)
BEGIN
INSERT INTO projects (name) SELECT project_name FROM DUAL WHERE project_name NOT IN (
		SELECT name FROM projects);
INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END;
//
