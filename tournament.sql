-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

CREATE TABLE tournaments (t_id serial PRIMARY KEY,
                          t_name text,
                          t_date date);

CREATE TABLE participants (p_id serial PRIMARY KEY,
                           p_name varchar(100),
                           p_hometown varchar(100));

CREATE TABLE rounds (round integer,
                     t_id integer references tournaments (t_id),
                     pair_id integer,
                     player integer references participants (p_id),
                     winner integer);

CREATE VIEW standings AS SELECT r.player, p.p_name, coalesce(sum(cast(r.winner as int)),0)
                                AS wins, coalesce(max(cast(r.round as int)),0) AS matches
                                FROM rounds AS r RIGHT JOIN participants AS p ON r.player = p.p_id
                                GROUP BY r.player, p.p_name ORDER BY wins DESC;

CREATE VIEW roster AS SELECT id, name FROM (SELECT r.player AS id, p.p_name
                      AS name, coalesce(sum(cast(r.winner AS int)),0)
                      AS wins, coalesce(max(cast(r.round as int)),0)
                      AS matches FROM rounds AS r RIGHT JOIN participants AS p
                      ON r.player = p.p_id GROUP BY r.player, p.p_name ORDER BY wins DESC) AS results;

