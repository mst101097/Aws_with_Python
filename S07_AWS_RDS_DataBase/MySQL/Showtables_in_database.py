import pymysql
conn =''
try:
    conn= pymysql.connect(
        host="mstdbinstance.coejywpn3aup.us-east-1.rds.amazonaws.com",
        user="admins",
        password="password",
        database ="mstdb"
    )
    print("Connect establish")

    mycursor = conn.cursor()

    mycursor.execute("SHOW TABLES;")

    for table in mycursor:
        print(table)

except pymysql.MySQLError as e:
    print(f"ERROR: Could not connect to MySQL instance. {e}")
finally:
    if conn:
        conn.close()
        print("Connection closed.")
