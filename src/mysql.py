#!/usr/bin/env python3

import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.110.175",
    user="mydba",
    passwd="mydba"
)

mycursor = mydb.cursor()

mycursor.execute("show databases;")