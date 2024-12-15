import pymysql

try:
    connection = pymysql.connect(host="127.0.0.1", user="root", password="Teja@9676", database="inflexion")
    
    if connection:
        print("Connection successful")

    cursor = connection.cursor()
    if cursor:
        print("Cursor object created")
    
    while True:
        new_id = int(input('Please enter the new id: '))

        check_query = "SELECT COUNT(*) FROM inflexion.credentials WHERE id = %s;"
        cursor.execute(check_query, (new_id,))
        result = cursor.fetchone()

        if result[0] > 0:
            print(f"The id {new_id} already exists, please choose a unique id.")
        else:
            break 

    while True:
        new_login_id = input('Please enter the new login_id you want: ')

        check_query = "SELECT COUNT(*) FROM inflexion.credentials WHERE login_id = %s;"
        cursor.execute(check_query, (new_login_id,))
        result = cursor.fetchone()

        if result[0] > 0:
            print(f"The login_id {new_login_id} already exists, please choose a unique login_id.")
        else:
            break 
    
    new_password=input("Please enter your password: ")
    insert_query = "INSERT INTO inflexion.credentials (id, login_id, password) VALUES (%s, %s, %s);"
    cursor.execute(insert_query, (new_id, new_login_id, new_password))
    
    connection.commit() 
    print("New credentials added successfully")

except pymysql.DatabaseError as e:
    print("Problem in SQL connection:", e)

