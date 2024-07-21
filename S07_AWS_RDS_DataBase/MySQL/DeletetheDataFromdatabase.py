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

    #delete the data from datbase
    sqlQuery = "DELETE FROM Person WHERE id = 1"
    #value = (name,lastname)

    mycursor.execute(sqlQuery)
    conn.commit()
    print(f'{mycursor.rowcount} row affected...')
    

except pymysql.MySQLError as e:
    print(f"ERROR: Could not connect to MySQL instance. {e}")
finally:
    if conn:
        conn.close()
        print("Connection closed.")