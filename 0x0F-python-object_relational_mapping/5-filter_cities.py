#!/usr/bin/python3

"""
SQL Fiilter by parsed String and usage of JOIN
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    passwd = argv[2]
    dbname = argv[3]

    mydb = MySQLdb.connect(host='localhost', user=username, passwd=passwd,
                           port=3306, db=dbname, charset="utf8")

    mycursor = mydb.cursor()
    query = "SELECT cities.name FROM cities\
        INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s ORDER BY cities.id ASC;"
    mycursor.execute(query, (argv[4],))

    Savings = mycursor.fetchall()

    print(",".join([name[0] for name in Savings]))

    mydb.commit()
    mycursor.close()
    mydb.close()
