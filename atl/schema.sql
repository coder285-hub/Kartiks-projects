DROP TABLE "Passengers"
DROP TABLE "Check-Ins"
DROP TABLE "Airlines"

CREATE TABLE Passengers (
    "id" INTEGER
    "first_name" TEXT
    "last_name" TEXT
    "age" INTEGER
    PRIMARY KEY("id")

);

CREATE TABLE Airlines(
    "id" INTEGER
    "name" TEXT
    "concourse" TEXT
    PRIMARY KEY("id")
);


CREATE TABLE Flights(
    "id" INTEGER,
    "flight_number" INTEGER,
    "airline_id"-INTEGER,
    "departing_airport_code" TEXT, -"arrival_airport_code" TEXT,
    "departing_datetime" DATETIME,
    "arrival_datetime", DATETIME,
    PRIMARY KEY("id")
    FOREIGN KEY ("airline_id") -REFERENCES Airlines("id")
);

CREATE TABLE Check-Ins (
    "id" INTEGER
    "datetime" 
)


