.import --csv meteorites.csv meteorites_temp

UPDATE meteorites_temp
SET "mass" =NULL
WHERE id =(
    SELECT id FROM meteorites_temp
    WHERE mass =""

);
