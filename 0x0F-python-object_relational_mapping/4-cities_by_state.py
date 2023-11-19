#!/usr/bin/python3

"""
joinig two tables
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
    query = "SELECT cities.id, cities.name, states.name FROM cities\
        INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC;"
    mycursor.execute(query)

    Savings = mycursor.fetchall()
    for saver in Savings:
        print(saver)

    mydb.commit()
    mycursor.close()
    mydb.close()
