#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
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
    cursor.execute("SELECT cities.name \
                   FROM cities \
                   INNER JOIN states ON cities.state_id = states.id \
                   WHERE states.name = %s \
                   ORDER BY cities.id ASC;", (sys.argv[4], ))

    id_cities = cursor.fetchall()
    print(', '.join(i[0] for i in id_cities))

    cursor.close()
    conn.close()
