#!/usr/bin/python3
"""
Lists all cities of a state on the DB hbtn_0e_4_usa
using the state as argument
Arguments:
    username - username to connect the mySQL
    mysql passwd - password to connect the mySQL
    DB name - Name of the database
    state name - name of the state to search
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    state_name = (argv[4], )
    cur.execute("SELECT * FROM cities\
                JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", state_name)
    lists = cur.fetchall()
    cities = []
    for row in lists:
        if row[4] == state_name[0]:
            cities.append(row[2])
    print(', '.join(cities))
    cur.close()
    db.close()
