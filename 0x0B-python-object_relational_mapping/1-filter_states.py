#!/usr/bin/python3
"""
    Script that lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


def print_stateN():
    """
    Print states from database
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '%N%'")
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    print_stateN()
