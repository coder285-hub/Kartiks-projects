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



