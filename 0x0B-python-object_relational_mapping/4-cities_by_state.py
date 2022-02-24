#!/usr/bin/python3
"""
list all cities from database htbn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    takes 3 arguments, uses module MySQLdb
    , connects to localhost and port 3306,
    results assorted in ascending order, can only use
    execute() once, does not execute when imported
    """
    datab = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                            passwd=argv[2], db=argv[3])
    with datab.cursor() as curse:
        curse.execute("""SELECT cities.id, cities.name, states.name FROM \
                        cities JOIN states ON cities.state_id = states.id \
                        ORDER BY cities.id ASC""")
        rows = curse.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
