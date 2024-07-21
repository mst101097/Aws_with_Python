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
    create_table_sql = """
    CREATE TABLE Person (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        lastname VARCHAR(255)
    );
    """
    mycursor.execute(create_table_sql)
    # mycursor.commit()
    print('table created')


    

except pymysql.MySQLError as e:
    print(f"ERROR: Could not connect to MySQL instance. {e}")
finally:
    if conn:
        conn.close()
        print("Connection closed.")
