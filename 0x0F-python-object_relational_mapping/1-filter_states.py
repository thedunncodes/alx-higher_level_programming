#!/usr/bin/python3

"""
SQL Fiilter by first letter function
"""

import MySQLdb
from sys import argv
if __name__ == '__main__':
    username = argv[1]
    passwd = argv[2]
    dbname = argv[3]

    mydb = MySQLdb.connect(host='localhost', user=username, passwd=passwd,
                           port=3306, db=dbname)

    mycursor = mydb.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%%' ORDER BY states.id ASC;"
    mycursor.execute(query)

    Savings = mycursor.fetchall()
    for saver in Savings:
        print(saver)

    mydb.commit()
    mycursor.close()
    mydb.close()
