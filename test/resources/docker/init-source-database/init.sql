create schema if not exists test;

CREATE TABLE test.movie
(
    title       text    NOT NULL,
    director   text    NOT NULL,
    year        integer NOT NULL,
    genre text    NOT NULL
);

INSERT INTO test.movie (title, director, year, genre)
values ('matrix', 'wachowski', 1999, 'action');

INSERT INTO test.movie (title, director, year, genre)
values ('goodfellas', 'scorsese', 1990, 'biography');

INSERT INTO test.movie (title, director, year, genre)
values ('se7en', 'fincher', 1995, 'crime');

INSERT INTO test.movie (title, director, year, genre)
values ('interstellar', 'nolan', 2014, 'adventure');

INSERT INTO test.movie (title, director, year, genre)
values ('psycho', 'hitchcock', 1960, 'horror');