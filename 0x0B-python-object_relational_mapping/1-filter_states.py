#!/usr/bin/python3
"""
Lists all states with a name that starts with N
uppercase only my guy from hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    getting state names from the database
    """
    datab = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                            passwd=argv[2], db=argv[3])
    curse = datab.cursor()
    curse.execute("SELECT * FROM states WHERE name LIKE BINARY \
                   'N%' ORDER BY states.id ASC")
    rows = curse.fetchall()
    for row in rows:
        print(row)
