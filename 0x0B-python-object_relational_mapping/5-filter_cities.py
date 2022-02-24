#!/usr/bin/python3
"""
takes in the name of a state as an arg and
lists all cities of that particular state
using datab hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    takes 4 arguments, uses module MySQLdb, connects
    to localhost at port 3306, results sorted in
    ascending order by cities.id, use excute only
    once, does not execute when imported
    """
    datab = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                            passwd=argv[2], db=argv[3])
    with datab.cursor() as curse:
        curse.execute("""SELECT cities.id, cities.name FROM \
                        cities JOIN states ON cities.state_id = states.id \
                        WHERE states.name LIKE BINARY %(state_name)s \
                        ORDER BY cities.id ASC""", {'state_name': argv[4]})
        rows = curse.fetchall()
    if rows is not None:
        print(", ".join([row[1] for row in rows]))
