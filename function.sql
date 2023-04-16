USE cosmetics;

-- 1.
DROP FUNCTION IF EXISTS check_username;
DELIMITER $$
CREATE FUNCTION check_username(username_p VARCHAR(150))
	RETURNS INT NOT DETERMINISTIC READS SQL DATA
    BEGIN
		DECLARE exist INT DEFAULT 0;
        SELECT COUNT(username) INTO exist FROM users_user WHERE username = username_p;
        RETURN (exist);
	END $$
DELIMITER ;

SELECT check_username('sam') FROM users_user;
SELECT check_username('daniel') FROM users_user;

-- 2.
DROP FUNCTION IF EXISTS check_superuser;
DELIMITER $$
CREATE FUNCTION check_superuser(username_p VARCHAR(150))
	RETURNS INT NOT DETERMINISTIC READS SQL DATA
    BEGIN
		DECLARE company INT DEFAULT 0;
        SELECT is_superuser INTO company FROM users_user WHERE username = username_p;
        RETURN (company);
	END $$
DELIMITER ;

SELECT * FROM users_user;
SELECT check_superuser('admin');
SELECT check_superuser('daniel');
SELECT * FROM cosapp_product;