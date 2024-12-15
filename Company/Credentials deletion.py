import pymysql

try:
    connection = pymysql.connect(host="127.0.0.1",user="root",password="Teja@9676",database="inflexion")
    if connection:
        print("Connection successful")
    
    cursor = connection.cursor()
    if cursor:
        print("Cursor object created")

    delete_id=int(input("Please enter the id that has to be deleted: "))
    query="DELETE FROM inflexion.credentials WHERE id =%s;"



    check_query = "SELECT COUNT(*) FROM inflexion.credentials WHERE id = %s;"
    cursor.execute(check_query, (delete_id,))
    result = cursor.fetchone()

    if result[0] !=1:
        print(f"The id {delete_id} doesnt exists")
    else:
        cursor.execute(query,(delete_id))
        print(f"id {delete_id} deleted from the table")

    connection.commit()
    


except pymysql.DatabaseError as e:
    print("Problem in SQL connection:", e)