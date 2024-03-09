
-- *** The Lost Letter ***
SELECT id FROM addresses
WHERE address LIKE "2 Fin%"

SELECT * FROM packages
WHERE from_address_id = (
    SELECT id FROM addresses -SELECT-id-FROM-addresses
    WHERE address = "900 Somerville Avenue"
)AND to_address_id = (
    SELECT id FROM addresses
    WHERE address LIKE "2 Fin%"
);

-- *** The Devious Delivery ***
SELECT FROM addresses
    WHERE id = (
    SELECT address_id FROM scans
    WHERE package_id=(
        SELECT id FROM packages
        WHERE from_address_id IS NULL
    )AND action = "Drop"
);


-- *** The Forgotten Gift ***

SELECT * FROM packages
WHERE from_address_id(
    SELECT id FROM addresses
    WHERE address = "109 Tileston Street"

);

