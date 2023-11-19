#!/usr/bin/python3

"""
SQL Fiilter by parsed String
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    passwd = argv[2]
    dbname = argv[3]
    nameRequest = argv[4]

    split = nameRequest.split(";")
    actualName = split[0]

    mydb = MySQLdb.connect(host='localhost', user=username, passwd=passwd,
                           port=3306, db=dbname, charset="utf8")

    mycursor = mydb.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    mycursor.execute(query, (actualName,))

    Savings = mycursor.fetchall()
    for saver in Savings:
        print(saver)

    mydb.commit()
    mycursor.close()
    mydb.close()
