
import pymysql

try:
    connection = pymysql.connect(host="127.0.0.1",user="root",password="Teja@9676",database="inflexion")
    if connection:
        print("Connection successful")
    
    cursor = connection.cursor()
    if cursor:
        print("Cursor object created")
    
    
    id=int(input("Please enter the id that password has to be change: "))
    new_password = input('Please enter the new password: ')

    query = "UPDATE inflexion.credentials SET password = %s WHERE id = %s"
    cursor.execute(query, (new_password, id))
    
    print("Password changed successfully")
    connection.commit()

except pymysql.DatabaseError as e:
    print("Problem in SQL connection:", e)

