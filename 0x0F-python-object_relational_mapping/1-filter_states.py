#!/usr/bin/python3

"""
Lists all states with the name
starting with N from the database hbtn_0e_0_usa
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
    cursor.execute("SELECT * FROM states;")

    id_states = cursor.fetchall()
    for i in id_states:
        if i[1].startswith('N'):
            print(i)
