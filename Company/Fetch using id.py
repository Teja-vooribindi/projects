import pymysql

try:
    connection = pymysql.connect(host="127.0.0.1",user="root",password="Teja@9676",database="inflexion")
    if connection:
        print("Connection successful")
    
    cursor = connection.cursor()
    if cursor:
        print("Cursor object created")

    fetch_id=int(input("Please enter the id that you need to fetch the details: "))
    query="SELECT * FROM inflexion.credentials WHERE id =%s;"
    cursor.execute(query,(fetch_id))
    connection.commit()
    data=cursor.fetchone()
    print(data
          )


except pymysql.DatabaseError as e:
    print("Problem in SQL connection:", e)