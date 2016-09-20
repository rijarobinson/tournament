#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def addTournament(t_name, t_date):
    """Extra credit: support more than one tournament. If function is called,"""
    """user can supply a name for the tournament and date the tournament is held."""
    con = connect()
    cur = con.cursor()
    add_tourney = ("INSERT INTO tournaments (t_name, t_date) VALUES (%s,%s);")
    cur.execute(add_tourney, (t_name,t_date,))
    con.commit()
    con.close()

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
    """create participant detail record"""
    create_partic = ("INSERT INTO participants (p_name) "
                        "VALUES (%s) RETURNING p_id;")
    cur.execute(create_partic, (player_name,))
    p_id = cur.fetchone()
    con.commit()
    """add player to rounds to associate with tournament """
    """and round (function to be added)"""
    add_to_rounds = ("INSERT INTO rounds (t_id, player, round, winner) "
                    "VALUES (%s,%s,%s,%s);")
    cur.execute(add_to_rounds, (tournament,p_id,0,0,))
    con.commit()
    con.close()

def playerStandings():
    """
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    con = connect()
    cur = con.cursor()
    """ Get the list of players and sort by number of wins """
    """ Round column is for future tracking of rounds played. """
    cur.execute("SELECT r.player, p.p_name, "
                "coalesce(sum(cast(r.winner as int)),0) AS wins, "
                "coalesce(max(cast(r.round as int)),0) AS matches FROM rounds "
                "AS r RIGHT JOIN participants AS p ON r.player = p.p_id "
                "GROUP BY r.player, p.p_name ORDER BY wins DESC;")
    standings = cur.fetchall()
    con.commit()
    con.close()
    return standings

def reportMatch(winner, loser, draw):
    """Records the outcome of a single match between two players.

    """
    """Attempted extra credit by including input for draw where both """
    """players are awarded a point for draw. Draw is set to True or False. """
    con = connect()
    cur = con.cursor()
    winner = bleach.clean(winner, strip=True)
    """get the highest number of rounds for the winner for later use"""
    get_winner_rounds = ("SELECT max(round) as curr_matches FROM rounds "
                            "WHERE player = (%s);")
    cur.execute(get_winner_rounds, (winner,))
    new_matches_winner = int(cur.fetchone()[0]) + 1
    """update query to be executed later"""
    set_winner = ("UPDATE rounds SET winner = (%s), round = (%s) "
                "WHERE player = (%s);")
    loser = bleach.clean(loser, strip=True)
    """get the highest number of rounds for the loser for later use."""
    get_loser_rounds = ("SELECT max(round) as curr_matches FROM rounds "
                        "WHERE player = (%s);")
    cur.execute(get_loser_rounds, (loser,))
    new_matches_loser = int(cur.fetchone()[0]) + 1
    """update query to be executed later"""
    set_loser = ("UPDATE rounds SET winner = (%s), round = (%s) "
            "WHERE player = (%s);")
    """If draw is set to True, both players are flagged as 1 (winner)"""
    if draw:
        """update rounds table with winner data"""
        cur.execute(set_winner, (1,new_matches_winner,winner,))
        """update rounds table with loser data"""
        cur.execute(set_loser, (1,new_matches_loser,loser,))
        """otherwise, the winner is flagged as 1 and loser flagged as 0"""
    else:
        """get the highest number of rounds for the winner for later use"""
        cur.execute(set_winner, (1,new_matches_winner,winner,))
        cur.execute(set_loser, (0,new_matches_loser,loser,))
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

    """TODO: only pair if pair does not match in any previous games."""
    """use player and pair_id.  so where combination of p_id and """
    """pair_id of each person in proposed pair has not been seen before. """
    """NOTE TO SELF: see saved_code.txt for stub"""

    con = connect()
    cur = con.cursor()
    cur.execute("SELECT id, name FROM (SELECT r.player as id, p.p_name as name, "
                "coalesce(sum(cast(r.winner as int)),0) AS wins, "
                "coalesce(max(cast(r.round as int)),0) AS matches "
                "FROM rounds AS r RIGHT JOIN participants AS p "
                "ON r.player = p.p_id GROUP BY r.player, p.p_name "
                "ORDER BY wins DESC) AS results;")
    standings = cur.fetchall()
    pairings_tuple = ()
    pairings_list = []
    pair = 0
    while pair < len(standings):
        """create the tuple and append to the list"""
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