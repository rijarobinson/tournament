#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    con = connect()
    cur = con.cursor()
    cur.execute("DELETE FROM rounds;")
    con.commit()
    con.close()


def deletePlayers():
    """Remove all the player records from the database."""
    con = connect()
    cur = con.cursor()
    cur.execute("DELETE FROM rounds;")
    cur.execute("DELETE FROM participants;")
    con.commit()
    con.close()


def countPlayers():
    """Returns the number of players currently registered."""
    con = connect()
    cur = con.cursor()
    num_partic = cur.execute("SELECT count(*) as num FROM participants;")
    counted = cur.fetchone()[0]
    con.close()
    return counted


def registerPlayer(name, tournament):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    con = connect()
    cur = con.cursor()
    player_name = bleach.clean(name, strip=True)
    cur.execute("INSERT INTO participants (p_name) VALUES (%s) RETURNING p_id;", (player_name,))
    p_id = cur.fetchone()
    con.commit()
    cur.execute("INSERT INTO rounds (t_id, player, round, winner) VALUES (%s,%s,%s,%s)", (tournament,p_id,0,0,))
    con.commit()
    con.close()



def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT r.player, p.p_name, coalesce(sum(cast(r.winner as int)),0) AS wins, coalesce(max(cast(r.round as int)),0) AS matches FROM rounds AS r RIGHT JOIN participants AS p ON r.player = p.p_id GROUP BY r.player, p.p_name ORDER BY wins DESC;")
    standings = cur.fetchall()
    con.commit()
    con.close()
    return standings

"""    standings = ({str(row[0]), str(row[1]), str(row[2]), str(r[3])},)"""



def reportMatch(winner, loser, draw):
    """Records the outcome of a single match between two players.

Need to update rounds table. update the record
by p_id, either winner or loser. update player field with winner or loser.
if it's the winner, put 1 into winner field. if it's the loser,
put 0 into winner field. Also need to insert round into round field.
get max of round and add 1 and include in update

"""
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT max(round) as curr_matches FROM rounds WHERE player = (%s)", (winner,))
    if draw:
        curr_matches = cur.fetchone()
        new_matches = int(curr_matches[0]) + 1
        winner = bleach.clean(winner, strip=True)
        cur.execute("UPDATE rounds SET winner = (%s), round = (%s) WHERE player = (%s)", (1,new_matches,winner,))
        cur.execute("SELECT max(round) as curr_matches FROM rounds WHERE player = (%s)", (loser,))
        curr_matches = cur.fetchone()
        new_matches = int(curr_matches[0]) + 1
        loser = bleach.clean(loser, strip=True)
        cur.execute("UPDATE rounds SET winner = (%s), round = (%s) WHERE player = (%s)", (1,new_matches,loser,))
    else:
        curr_matches = cur.fetchone()
        new_matches = int(curr_matches[0]) + 1
        winner = bleach.clean(winner, strip=True)
        cur.execute("UPDATE rounds SET winner = (%s), round = (%s) WHERE player = (%s)", (1,new_matches,winner,))
        cur.execute("SELECT max(round) as curr_matches FROM rounds WHERE player = (%s)", (loser,))
        curr_matches = cur.fetchone()
        new_matches = int(curr_matches[0]) + 1
        loser = bleach.clean(loser, strip=True)
        cur.execute("UPDATE rounds SET winner = (%s), round = (%s) WHERE player = (%s)", (0,new_matches,loser,))
    con.commit()
    con.close()

"""
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings."""

    con = connect()
    cur = con.cursor()
    cur.execute("SELECT id, name FROM (SELECT r.player as id, p.p_name as name, coalesce(sum(cast(r.winner as int)),0) AS wins, coalesce(max(cast(r.round as int)),0) AS matches FROM rounds AS r RIGHT JOIN participants AS p ON r.player = p.p_id GROUP BY r.player, p.p_name ORDER BY wins DESC) AS results;")
    standings = cur.fetchall()
    cur.execute("SELECT coalesce(max(cast(pair_id as int)),0) AS pair_id FROM rounds;")
    max_pair_id = cur.fetchone()
    new_pair_id = int(max_pair_id[0]) + 1
    pairings_tuple = ()
    pairings_list = []
    pair = 0
    """only pair if pair does not match in any previous games. use p_id and pair_id.  so where combination of p_id and
        pair_id of each person in proposed pair has not been seen before."""
    while pair < len(standings):
        pairings_tuple = ({standings[pair] + standings[pair + 1]})
        pairings_list.extend(pairings_tuple)
        pair = pair + 2
    con.close()
    return pairings_list

"""    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


