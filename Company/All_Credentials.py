import pymysql

try:
    connection = pymysql.connect(host="127.0.0.1",user="root",password="Teja@9676",database="inflexion")
    if connection:
        print("Connection successful")
    
    cursor = connection.cursor()
    if cursor:
        print("Cursor object created")

    query="SELECT * FROM inflexion.credentials;"
    cursor.execute(query)
    connection.commit()
    data=cursor.fetchall()
    for i in data:
        print(i)


except pymysql.DatabaseError as e:
    print("Problem in SQL connection:", e)