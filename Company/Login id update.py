import pymysql

try:
    connection = pymysql.connect(host="127.0.0.1", user="root", password="Teja@9676", database="inflexion")
    if connection:
        print("Connection successful")

    cursor = connection.cursor()
    if cursor:
        print("Cursor object created")

    update_query = "UPDATE inflexion.credentials SET login_id = %s WHERE id = %s"

    while True:
        new_login_id = input('Please enter the new login_id you want: ')

        check_query = "SELECT COUNT(*) FROM inflexion.credentials WHERE login_id = %s"
        cursor.execute(check_query, (new_login_id,))
        result = cursor.fetchone()

        if result[0] > 0:
            print(f"The login_id '{new_login_id}' already exists, please choose a unique login_id.")
        else:
            id = int(input("Please enter the id whose login_id needs to be changed: "))
            
            cursor.execute(update_query, (new_login_id, id))
            connection.commit()
            print("Login_id updated successfully")
            break

except pymysql.DatabaseError as e:
    print("Problem in SQL connection:", e)


