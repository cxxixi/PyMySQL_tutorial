import pandas as pd 

import mysql.connector
from mysql.connector import Error

def connect(db):
    try:
        conn=mysql.connector.connect(host='YOUR HOST',
                                     database=YOUR DATABASE,
                                     user='root',
                                     password='YOUR PASSWORD')
        if conn.is_connected():
            print('connected to the database!')
    except Error as e:
        print(e)
    finally:
        conn.close()

def create_database(cursor):
	try:
		cursor.execute(
			"CREATE DATABASE{} ".format(wechat))
	except Error as e:
		print e

def create_tables():
	try:
		order1 = 'CREATE TABLE IF NOT EXISTS house_info(
					house_id INT(5) NOT NULL AUTO_INCREMENT
					house_owner VARCHAR(10) NOT NULL
					house_di
		)
		'
		order2 = 'CREATE TABLE IF NOT EXISTS house_feature'
		order3 = 'location


TABLES = {}
TABLES['message'] = (
	"CREATE TABLE message("
		"contact_id INT(3) NOT NULL"
		"message_id INT(6) NOT NULL AUTO_INCREMENT,"
		"sent_date DATE NOT NULL"
		"time "
		"PRIMARY KEY(contact_id)"

	)




