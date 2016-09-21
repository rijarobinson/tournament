-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP TABLE IF EXISTS tournaments CASCADE;
DROP TABLE IF EXISTS participants CASCADE;
DROP TABLE IF EXISTS rounds;

CREATE TABLE tournaments (t_id serial PRIMARY KEY, t_name text, t_date date);

CREATE TABLE participants (p_id serial PRIMARY KEY, p_name varchar(100), p_hometown varchar(100));

CREATE TABLE rounds (round integer, t_id integer
    references tournaments (t_id), pair_id integer, player integer
    references participants (p_id), winner integer);

