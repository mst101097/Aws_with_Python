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
    name = input("Input the employee name: ")
    lastname = input("Input the lastanme: ")

    sqlQuery = "INSERT INTO Person(name , lastname) VALUES(%s,%s)"
    value = (name,lastname)

    mycursor.execute(sqlQuery,value)
    conn.commit()
    print('data inserted ')

except pymysql.MySQLError as e:
    print(f"ERROR: Could not connect to MySQL instance. {e}")
finally:
    if conn:
        conn.close()
        print("Connection closed.")