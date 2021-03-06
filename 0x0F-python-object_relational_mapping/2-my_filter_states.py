#!/usr/bin/python3
'''
Write a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where name
matches the argument
'''
if __name__ == "__main__":
    import sys
    import MySQLdb
    # take arguments
    args = sys.argv
    try:
        user = args[1]
        password = args[2]
        database = args[3]
        nameSearch = args[4]
        db = MySQLdb.connect(
                            host="localhost",
                            port=3306,
                            user=user,
                            passwd=password,
                            db=database)
        cur = db.cursor()
        cur.execute("SELECT * FROM states "
                    "WHERE name LIKE BINARY '{}' "
                    "ORDER BY id ASC".format(nameSearch))

        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()

    except:
        pass
