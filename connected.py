import mysql.connector
from mysql.connector import Error


def connect(db):
    try:
        conn=mysql.connector.connect(host='YOUR HOST',
                                     database=YOUR SPECIFIC DATABASE',
                                     user='USER NAME, DEDEAULT IS root',
                                     password='YOUR PASSWORD')
        if conn.is_connected():
            print('connected to the database!')
    except Error as e:
        print(e)
    finally:
        conn.close()

connect('YOUR DATABASE NAME')
