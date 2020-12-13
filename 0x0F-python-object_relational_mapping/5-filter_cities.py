#!/usr/bin/python3
'''
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
'''
if __name__ == "__main__":
    import sys
    import MySQLdb
    # take arguments
    args = sys.argv
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
    cur.execute("SELECT cities.name "
                "FROM cities JOIN states "
                "ON cities.state_id = states.id "
                "WHERE states.name LIKE BINARY %(nameSearch)s "
                "ORDER BY cities.id ASC", {'nameSearch': nameSearch})
    rows = cur.fetchall()
    print(", ".join(map(lambda row: row[0], rows)))
    cur.close()
    db.close()
