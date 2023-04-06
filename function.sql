USE cosmetics;

DROP FUNCTION IF EXISTS check_username;
DELIMITER $$
CREATE FUNCTION check_username(username_p VARCHAR(150))
	RETURNS INT NOT DETERMINISTIC READS SQL DATA
    BEGIN
		DECLARE exist INT DEFAULT 0;
        SELECT COUNT(username) INTO exist FROM users_user WHERE username = username_p ;
        RETURN (exist);
	END $$
DELIMITER ;

SELECT check_username('sam') FROM users_user;
SELECT check_username('daniel') FROM users_user;