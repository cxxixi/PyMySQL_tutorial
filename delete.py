from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
def delete_book(title):
    query = "DELETE FROM books WHERE title=%s"
 
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query, (title,))

        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
delete_book('A Sudden Light')
