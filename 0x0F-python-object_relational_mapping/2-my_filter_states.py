#!/usr/bin/python3

"""
Displays all values in the states from the table of hbtn_0e_0_usa
where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        port=3306,
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states\
                   WHERE name LIKE '{}';".format(sys.argv[4]))

    id_states = cursor.fetchall()
    for i in id_states:
        print(i)
