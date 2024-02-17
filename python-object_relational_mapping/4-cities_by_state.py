#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


def list_states(username, password, dbname):
    """
    Lists all states from the database.
    """
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=dbname)

    # Create a cursor object
    cur = db.cursor()

    # Execute the query using parameterized SQL statement
    query = "SELECT cities.id, cities.name, states.name " \
            "FROM cities INNER JOIN  states ON " \
            "cities.state_id = states.id " \
            "ORDER BY cities.id ASC"

    # Execute the query
    cur.execute(query)

    # Fetch and print all rows that match the query
    for row in cur.fetchall():
        print(row)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        list_states(username, password, dbname)
