-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP database IF EXISTS tournament;

CREATE database tournament;

CREATE TABLE tournaments (t_id serial PRIMARY KEY, t_name text, t_year date);

CREATE TABLE participants (p_id serial PRIMARY KEY, p_name varchar(25), p_hometown varchar(100));

-- no longer using this table. CREATE TABLE registration (t_id integer references tournaments (t_id), p_id integer references participants (p_id));

CREATE TABLE rounds (round integer, t_id integer
    references tournaments (t_id), pair_id integer, player integer
    references participants (p_id), winner integer);



-- A list of tuples, each of which contains (id, name, wins, matches):
--        id: the player's unique id (assigned by the database)
--        name: the player's full name (as registered)
--        wins: the number of matches the player has won
--        matches: the number of matches the player has played

--rounds:
--p_id -> participants -> p_name

--wins is a count(winner) as wins from rounds group by winner
--matches is a count(*) as matches from rounds where player_1 = winner or player_2 = winner

--CREATE VIEW standings as SELECT registration.p_id, count(*) as wins FROM rounds LEFT JOIN registration ON registration.p_id = rounds.winner
--    WHERE registration.t_id = 1 group by winner order by wins desc;

select rounds.player_1, p.p_name as p_name_1, p.p_id as p_id_1,
    rounds.player_2, p2.p_name as p_name_2, p2.p_id as p_id_2
    from rounds join participants as p on rounds.player_1 = p.p_id
    inner join participants as p2 on rounds.player_2 = p2.p_id;


id, name, wins, matches
select r.player, p.p_name, sum(r.winner) as wins, max(r.round) as matches from rounds as r left join participants as p on r.player = p.p_id where r.t_id = 1 group by r.player, p.p_name order by wins desc;

select * from tournament;

select * from participants;

select * from registration;

select * from rounds;

insert into participants (p_name, p_hometown) values ('Marija','Highland Park'), ('Ian','Highland Park'),('Amanda','Bolingbrook'),('Ben','Bolingbrook');

insert into registration values (1,12), (1,13),(1,14),(1,15),(1,16),(1,17);

insert into rounds values(3,1,1,12,0),
                            (3,1,1,13,1),
;

insert into rounds values(1,1,1,12,0),(1,1,1,13,1),(1,1,2,14,0),(1,1,2,15,1),(1,1,3,16,1),(1,1,3,17,0),(2,1,1,12,0),(2,1,1,14,1),(2,1,2,13,0),(2,1,2,15,1),(2,1,3,16,0),(2,1,3,17,1);

insert into rounds values(3,1,1,12,0),(3,1,1,13,1);


        select count(*) from participants;

