CREATE TABLE users (
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "username" TEXT NOT NULL UNIQUE,
    "password" TEXT NOT NULL,
    Primary Key("id")
);

CREATE TABLE Schools (
    "id" INTEGER NOT NULL,
    "name" TEXT NOT NULL,
    "type" TEXT,
    "location" TEXT,
    "year_founded" NUMERIC,
    Primary Key("id")
);

CREATE TABLE Companies (
    "id" INTEGER NOT NULL,
    "name" TEXT NOT NULL UNIQUE,
    "Industry" TEXT NOT NULL,
    "Location" TEXT NOT NULL,
);

CREATE TABLE people_connections (
    "id" INTEGER,
    "user_id" INTEGER,
    "following_id" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("user_id") REFERENCES users("id"),
    FOREIGN KEY("following_id") REFERENCES users("id"),
    CONSTRAINT unique_connection UNIQUE (user_id, following_id)
);

CREATE TABLE school_connections (
    "id" INTEGER,
    "user_id" INTEGER,
    "school_id" INTEGER,
    "start_date" DATE,
    "end_date" DATE,
    "degree_type" TEXT,
    PRIMARY KEY("id"),
    FOREIGN KEY("user_id") REFERENCES users("id"),
    FOREIGN KEY("school_id") REFERENCES Schools("id"),
    CONSTRAINT unique_school_connection UNIQUE (user_id, school_id)
);
CREATE TABLE company_connections (
    "id" INTEGER,
    "user_id" INTEGER,
    "company_id" INTEGER,
    "start_date" DATE,
    "end_date" DATE,
    "company_type" TEXT,
    PRIMARY KEY("id"),
    FOREIGN KEY("user_id") REFERENCES users ("id"),
    FOREIGN KEY("company_id") REFERENCES Companies ("id"),
    CONSTRAINT unique_comapny_connection UNIQUE (user_id, company_id)
);




