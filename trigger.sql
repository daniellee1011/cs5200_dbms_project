-- Trigger for counting number of reviews after insert
DROP TRIGGER IF EXISTS numReviews_after_review_insert;
DELIMITER $$

CREATE TRIGGER numReviews_after_review_insert
AFTER INSERT ON cosapp_userreview
FOR EACH ROW
BEGIN
	
    DECLARE num_review INT;
    SELECT COUNT(*) INTO num_review FROM cosapp_userreview WHERE cosapp_userreview.product_id = NEW.product_id;
	UPDATE cosapp_product SET numReviews = num_review WHERE cosapp_product.id = NEW.product_id;
 
END$$

DELIMITER ;

-- Trigger for counting number of reviews after delete
DROP TRIGGER IF EXISTS numReviews_before_review_delete;
DELIMITER $$

CREATE TRIGGER numReviews_before_review_delete
AFTER DELETE ON cosapp_userreview
FOR EACH ROW
BEGIN
	
    DECLARE num_review INT;
    SELECT COUNT(*) INTO num_review FROM cosapp_userreview WHERE cosapp_userreview.product_id = OLD.product_id;
	UPDATE cosapp_product SET numReviews = num_review WHERE cosapp_product.id = OLD.product_id;
 
END$$

DELIMITER ;

-- Trigger for calculating average rating after insert
DROP TRIGGER IF EXISTS avgRating_after_review_insert;
DELIMITER $$

CREATE TRIGGER avgRating_after_review_insert
AFTER INSERT ON cosapp_userreview
FOR EACH ROW
BEGIN
	
    DECLARE avg_rate DECIMAL(10,2);
    SELECT AVG(stars) INTO avg_rate FROM cosapp_userreview WHERE cosapp_userreview.product_id = NEW.product_id;
	UPDATE cosapp_product SET avgRating = avg_rate WHERE cosapp_product.id = NEW.product_id;
 
END$$

DELIMITER ;

-- Trigger for calculating average rating after update
DROP TRIGGER IF EXISTS avgRating_after_review_update;
DELIMITER $$

CREATE TRIGGER avgRating_after_review_update
AFTER UPDATE ON cosapp_userreview
FOR EACH ROW
BEGIN
	
    DECLARE avg_rate DECIMAL(10,2);
    SELECT AVG(stars) INTO avg_rate FROM cosapp_userreview WHERE cosapp_userreview.product_id = NEW.product_id;
	UPDATE cosapp_product SET avgRating = avg_rate WHERE cosapp_product.id = NEW.product_id;
 
END$$

DELIMITER ;

-- Trigger for calculating average rating after delete
DROP TRIGGER IF EXISTS avgRating_before_review_delete;
DELIMITER $$

CREATE TRIGGER avgRating_before_review_delete
AFTER DELETE ON cosapp_userreview
FOR EACH ROW
BEGIN
	
    DECLARE avg_rate DECIMAL(10,2);
    SELECT AVG(stars) INTO avg_rate FROM cosapp_userreview WHERE cosapp_userreview.product_id = OLD.product_id;
    IF avg_rate IS NULL THEN SET avg_rate = 0;
	END IF;
	UPDATE cosapp_product SET avgRating = avg_rate WHERE cosapp_product.id = OLD.product_id;

END$$

DELIMITER ;