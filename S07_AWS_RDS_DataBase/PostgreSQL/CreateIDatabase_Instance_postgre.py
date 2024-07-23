import psycopg2

try:
    conn = psycopg2.connect(
        user = "",
        password = "",
        host="",
        port = 5432 )

    conn.autocommit = True

    mycursor = conn.cursor()

    query = "CREATE DATABASE mydb"

    mycursor.execute(query)



except:
    print("connection not establish..")