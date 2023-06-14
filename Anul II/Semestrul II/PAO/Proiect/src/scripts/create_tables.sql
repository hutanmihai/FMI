CREATE TABLE theater
(
    id            SERIAL PRIMARY KEY,
    name          VARCHAR(255),
    numberOfSeats INTEGER
);

CREATE TABLE employee
(
    id       SERIAL PRIMARY KEY,
    name     VARCHAR(255),
    email    VARCHAR(255),
    phone    VARCHAR(255),
    position VARCHAR(255),
    salary   INTEGER
);

CREATE TABLE client
(
    id            SERIAL PRIMARY KEY,
    name          VARCHAR(255),
    email         VARCHAR(255),
    phone         VARCHAR(255),
    membership    VARCHAR(255),
    loyaltyPoints INTEGER
);

CREATE TABLE movie
(
    id       SERIAL PRIMARY KEY,
    title    VARCHAR(255),
    genre    VARCHAR(255),
    year     INTEGER,
    duration INTEGER
);


CREATE TABLE showtime
(
    id          SERIAL PRIMARY KEY,
    theaterId   INTEGER REFERENCES theater (id) ON DELETE CASCADE,
    movieId     INTEGER REFERENCES movie (id) ON DELETE CASCADE,
    showingDate DATE,
    seats       INTEGER[]
);

CREATE TABLE snack
(
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(255),
    description VARCHAR(255),
    quantity    INTEGER,
    price       DOUBLE PRECISION,
    type        VARCHAR(255),
    size        VARCHAR(255)
);

CREATE TABLE soda
(
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(255),
    description VARCHAR(255),
    quantity    INTEGER,
    price       DOUBLE PRECISION,
    brand       VARCHAR(255),
    flavor      VARCHAR(255),
    volume      DOUBLE PRECISION
);

CREATE TABLE ticket
(
    id         SERIAL PRIMARY KEY,
    showtimeId INTEGER REFERENCES showtime (id) ON DELETE CASCADE,
    clientId   INTEGER REFERENCES client (id) ON DELETE CASCADE,
    employeeId INTEGER REFERENCES employee (id) ON DELETE CASCADE,
    price      DOUBLE PRECISION,
    seat       INTEGER
);
