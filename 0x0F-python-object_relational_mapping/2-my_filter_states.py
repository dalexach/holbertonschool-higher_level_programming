#!/usr/bin/python3
"""
Display all values in the states table of hbtn_0e_0_usa
where name matches the argument
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
    cur.execute("SELECT * FROM states WHERE name = '{}'\
                ORDER BY states.id ASC".format(argv[4]))
    lists = cur.fetchall()
    for row in lists:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
