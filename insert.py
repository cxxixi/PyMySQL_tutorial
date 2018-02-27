from mysql.connector import MySQLConnection,Error
from python_mysql_dbconfig import read_db_config

def insert_data(name,countrycode,district,population):
    query="INSERT INTO city(name,countrycode,district,population)" \
           "VALUES(%s,%s,%s,%s)"
    param=(name,countrycode,district,population)
    
    try:
        dbconfig=read_db_config()
        conn=MySQLConnection(**dbconfig)
        cursor=conn.cursor()
        cursor.execute(query,param)

        if cursor.lastrowid:
            print('last row id is',cursor.lastrowid)

        conn.commit()
                    
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def main():
    insert_data('5','5','5','1')
    
main()
