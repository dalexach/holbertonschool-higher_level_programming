#!/usr/bin/python3
"""
Display all values in the states table of hbtn_0e_0_usa
where name matches the argument
SQL injections
Arguments:
    username - username to connect the mySQL
    mysql passwd - password to connect the mySQL
    DB name - Name of the database
    name - state name searched
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    name = (argv[4], )
    cur.execute("SELECT * FROM states WHERE name = %s\
                ORDER BY states.id ASC", name)
    lists = cur.fetchall()
    for row in lists:
        print(row)
    cur.close()
    db.close()
