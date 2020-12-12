#!/usr/bin/python3
'''
script that lists all states from the database hbtn_0e_0_usa
'''

if __name__ == "__main__":
    import sys
    import MySQLdb
    # take arguments:
    args = sys.argv
    user = args[1]
    password = args[2]
    database = args[3]

    db = MySQLdb.connect(
                            host="localhost",
                            port=3306,
                            user=user,
                            passwd=password,
                            db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
