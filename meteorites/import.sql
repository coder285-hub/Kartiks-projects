.import --csv meteorites.csv meteorites_temp

UPDATE meteorites_temp
SET mass ="NULL"
where mass =0;

UPDATE meteorites_temp
SET year ="NULL"
where year LIKE '';

UPDATE meteorites_temp
SET lat ="NULL"
where lat =0;

UPDATE meteorites_temp
SET long ="NULL"
where long =0;

UPDATE meteorites_temp
SET mass = ROUND (mass,2),
    lat = ROUND (lat,2),
    long = ROUND (long,2);

CREATE TABLE meteorites (

    id INTEGER,
    name TEXT,
    class TEXT,
    mass REAL,
    discovery TEXT,
    year INTEGER,
    lat REAL,
    long REAL
    PRIMARY KEY('id')
);

INSERT INTO "meteorites" ("name", "class", "mass", "discovery", "year", "lat", "long")
SELECT "name", "class", "mass", "discovery", "year", "lat", "long"
FROM "meteorites_temp"
WHERE "nametype" != 'Relict'
ORDER BY "year", "name";



