#!/usr/bin/python3
"""
takes an argument and displays the vakue in states
table htbn_0e_0_usa where the name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    taking in arguments and displaying value
    """
    datab = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                            passwd=argv[2], db=argv[3])
    curse = datab.cursor()
    curse.execute("SELECT * FROM states WHERE name LIKE BINARY \
                   '{}' ORDER BY states.id ASC".format(argv[4]))
    rows = curse.fetchall()
    for row in rows:
        print(row)
