#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def list_states(username, password, dbname, state):
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
    #query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        
    #Directly using format with user input for SQL queries 
    # is not recommended due to the risk of SQL injection.
    # However, for educational purposes or specific cases 
    # where SQL injection risk is managed by other means, 
    # you can use string formatting to include variables in your query.
    
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state.replace("'", "''"))
    print(query);
    
    # Execute the query
    cur.execute(query, (state,))
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
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        state = sys.argv[4]
        list_states(username, password, dbname, state)
