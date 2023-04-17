use cosmetics;

-- 1.
DROP PROCEDURE IF EXISTS update_profile;
DELIMITER ??
CREATE PROCEDURE update_profile(username_p VARCHAR(150), email_p VARCHAR(254), nickname_p VARCHAR(30), age_p INT, gender_p VARCHAR(10), skin_type_p VARCHAR(30), address_p VARCHAR(50))
BEGIN
	UPDATE users_user SET
        email = email_p,
        nickname = nickname_p,
        age = age_p,
        gender = gender_p,
        skin_type = skin_type_p,
        address = address_p
        WHERE username = username_p;
END ??
DELIMITER ;

SELECT * FROM users_user WHERE username = 'daniel';
CALL update_profile('daniel', 'nor@eas.com', 'hi', 10, 'man', 'dry', 'longwood');

-- 'email', 'nickname', 'age', 'gender', 'skin_type', 'address'
-- cursor.callproc('update_profile', [profile_id, form.cleaned_data['email'], form.cleaned_data['nickname'], form.cleaned_data['age'], form.cleaned_data['gender'], form.cleaned_data['skin_type'], form.cleaned_data['address']])

-- 2.
DROP PROCEDURE IF EXISTS search_product_by_name;
DELIMITER $$
CREATE PROCEDURE search_product_by_name(name_p VARCHAR(50))
BEGIN
	SELECT * FROM cosapp_product WHERE name LIKE CONCAT('%', name_p, '%');
END $$
DELIMITER ;

SELECT * FROM cosapp_product WHERE name LIKE '%cream%';
CALL search_product_by_name('cream');

-- 3.
DROP PROCEDURE IF EXISTS search_review_by_user;
DELIMITER $$
CREATE PROCEDURE search_review_by_user(user_id_p BIGINT)
BEGIN
	SELECT r.*, p.name FROM cosapp_userreview AS r
		LEFT JOIN cosapp_product AS p
        ON r.product_id = p.id
        WHERE user_id = user_id_p;
END $$
DELIMITER ;

SELECT * FROM users_user;
SELECT * FROM cosapp_userreview;
CALL search_review_by_user(2);
SELECT r.*, p.name FROM cosapp_userreview AS r
	LEFT JOIN cosapp_product AS p ON r.product_id = p.id
	WHERE user_id = 2;

-- 4.
DROP PROCEDURE IF EXISTS insert_product;
DELIMITER $$
CREATE PROCEDURE insert_product(productType_p VARCHAR(150), cosmeticBrand_p VARCHAR(150), name_p VARCHAR(150), price_p DECIMAL(10, 2), size_p VARCHAR(10), avgRating_p DECIMAL(10, 2), numReviews_p INT, ingredients_p LONGTEXT)
BEGIN
	DECLARE productType_id_p, cosmeticBrand_id_p BIGINT;

    SELECT id INTO productType_id_p FROM cosapp_producttype WHERE typeName = productType_p;
    SELECT id INTO cosmeticBrand_id_p FROM cosapp_cosmeticbrand WHERE brandName = cosmeticBrand_p;

	INSERT INTO cosapp_product(
		name, price, size, avgRating, numReviews, ingredients, productType_id, cosmeticBrand_id)
		VALUES(name_p, price_p, size_p, avgRating_p, numReviews_p, ingredients_p, productType_id_p, cosmeticBrand_id_p);
END $$
DELIMITER ;

SELECT * FROM cosapp_product;
SELECT * FROM cosapp_producttype;
SELECT * FROM cosapp_cosmeticbrand;
INSERT INTO cosapp_product(
		name, price, size, avgRating, numReviews, ingredients, productType_id, cosmeticBrand_id)
		VALUES('cetaphil', 40.12, '19ml', 4.32, 0, 'moisturizing', 1, 1);

-- 5.
DROP PROCEDURE IF EXISTS edit_product;
DELIMITER $$
CREATE PROCEDURE edit_product(productId_p BIGINT, productType_p VARCHAR(150), cosmeticBrand_p VARCHAR(150), name_p VARCHAR(150), price_p DECIMAL(10, 2), size_p VARCHAR(10), ingredients_p LONGTEXT)
BEGIN
	DECLARE productType_id_p, cosmeticBrand_id_p BIGINT;

    SELECT id INTO productType_id_p FROM cosapp_producttype WHERE typeName = productType_p;
    SELECT id INTO cosmeticBrand_id_p FROM cosapp_cosmeticbrand WHERE brandName = cosmeticBrand_p;

	UPDATE cosapp_product 
	SET
	productType_id = productType_id_p,
	cosmeticBrand_id = cosmeticBrand_id_p,
	name = name_p,
	price = price_p,
	size = size_p,
	ingredients = ingredients_p
	WHERE
	id = productId_p; 

END $$
DELIMITER ;
