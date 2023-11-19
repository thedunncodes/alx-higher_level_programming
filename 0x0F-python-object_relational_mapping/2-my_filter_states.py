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

    mydb = MySQLdb.connect(host='localhost', user=username, passwd=passwd,
                           port=3306, db=dbname)

    mycursor = mydb.cursor()
    query = "SELECT * FROM states WHERE states.name LIKE BINARY '{}'\
        ORDER BY states.id ASC;".format(nameRequest)
    mycursor.execute(query)

    Savings = mycursor.fetchall()
    for saver in Savings:
        print(saver)

    mydb.commit()
    mycursor.close()
    mydb.close()
