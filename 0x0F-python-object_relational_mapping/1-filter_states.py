#!/usr/bin/python3
"""
Filter all states from DB hbtn_0e_usa
with a name starting with N.
Arguments:
    username - username to connect the mySQL
    mysql passwd - password to connect the mySQL
    DB name - Name of the database
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE 'N%'\
                ORDER BY states.id ASC""")
    lists = cur.fetchall()
    for row in lists:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
