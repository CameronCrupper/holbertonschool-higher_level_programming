#!/usr/bin/python3
"""
takes in arguments and displays all values in states
table of hbtn_0e_0_usa where name mathces argument,
BUT its safe from MySQL injections
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    getting states from db.....but its safe
    """
    datab = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                            passwd=argv[2], db=argv[3])
    with datab.cursor() as curse:
        curse.execute("""SELECT * FROM states WHERE name LIKE BINARY \
        %(name)s ORDER BY states.id ASC""", {'name': argv[4]})
        rows = curse.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
