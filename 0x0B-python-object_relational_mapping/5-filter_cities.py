#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def filter_cities():
    """
    Method to list cities
    """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])

    cur = db.cursor()
    state = sys.argv[4]

    cur.execute("SELECT name FROM cities\
                    WHERE state_id =\
                        (SELECT id FROM states WHERE name = %(name)s)\
                            ORDER BY cities.id ASC", {'name': state})

    if rows := cur.fetchall():
        print(", ".join([record[0] for record in rows]))

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_cities()
