import pymysql

def mysql_connection():
    try:
        connection = pymysql.connect(
            host="localhost",  
            database="inflexion",    
            user="root",        
            password="Teja@9676" 
        )
        
        print("Connection successful:", connection)
        
        return connection
    except pymysql.MySQLError as e:  
        print("There is a problem with database connectivity:", e)

def create_cursor():

    try:
        connection = mysql_connection()
        if connection:
            cursor = connection.cursor()
            print("Cursor object created successfully:", cursor)
            return cursor

    except pymysql.DatabaseError as e:
        print("Unable to connect to the database:", e)

create_cursor()
