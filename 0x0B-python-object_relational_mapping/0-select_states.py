#!/usr/bin/python3
"""
listing all states from htbn_0e_0_usa database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Accessing database to get the states
    """
    datab = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                            passwd=argv[2], db=argv[3])
    curse = datab.cursor()
    curse.execute("SELECT * FROM states")
    rows = curse.fetchall()
    for row in rows:
        print(row)
