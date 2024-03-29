#!/usr/bin/python3

"""
SQL Fiilter function
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
    mycursor.execute('SELECT * FROM states ORDER BY states.id ASC')

    Savings = mycursor.fetchall()
    for saver in Savings:
        print(saver)

    mydb.commit()
    mycursor.close()
    mydb.close()
