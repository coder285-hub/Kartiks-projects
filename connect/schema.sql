CREATE TABLE users (
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "username" TEXT NOT NULL UNIQUE
    "password" TEXT NOT NULL
    Primary Key ("id")
);

CREATE TABLE Schools (
    "id" INTEGER NOT NULL,
    "name" TEXT NOT NULL,
    "type" TEXT,
    "location" TEXT,
    "year_founded" NUMERIC,
    Primary Key ("id")
);

CREATE TABLE Companies (
    "id" INTEGER NOT NULL,
    "name" TEXT NOT NULL UNIQUE,
    "Industry" TEXT NOT NULL,
    "Location" TEXT NOT NULL,
);


