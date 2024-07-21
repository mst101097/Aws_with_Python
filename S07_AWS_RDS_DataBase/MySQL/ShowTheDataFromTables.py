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

    sqlQuery = "SELECT * FROM Person"
    #value = (name,lastname)

    mycursor.execute(sqlQuery)

    for data in mycursor.fetchall():
        print(data)

except pymysql.MySQLError as e:
    print(f"ERROR: Could not connect to MySQL instance. {e}")
finally:
    if conn:
        conn.close()
        print("Connection closed.")