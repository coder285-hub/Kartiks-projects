CREATE TABLE "meteorites_temp" (
    id INTEGER,
    name TEXT,
    nametype TEXT,
    class TEXT,
    mass REAL,
    discovery TEXT,
    year INTEGER,
    lat REAL,
    long REAL
    Primary Key ('id')
);

.import --csv meteorites.csv meteorites_temp

UPDATE meteorites_temp
SET mass ="NULL"
where mass =0;

UPDATE meteorites_temp
SET year ="NULL"
where year =0;

UPDATE meteorites_temp
SET lat ="NULL"
where lat =0;

UPDATE meteorites_temp
SET long ="NULL"
where long =0;



