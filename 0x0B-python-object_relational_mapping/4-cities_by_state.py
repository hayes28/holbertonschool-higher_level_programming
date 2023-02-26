#!/usr/bin/python3
"""
Script that lists all cities
from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def print_cities():
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                LEFT JOIN states ON cities.state_id = states.id")
    for row in cur.fetchall():
        print(row)

        cur.close()
        db.close()


if __name__ == "__main__":
    print_cities()
