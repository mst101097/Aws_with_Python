import pymysql
# import mysql.connector as mc

# try:
#     mydb = ms.connect(
#         host="mstdbinstance.coejywpn3aup.us-east-1.rds.amazonaws.com",
#         user="admins",
#         password="password"
#     )

#     dbname = input("Please enter your database.")

#     cursor = mydb.cursor()

#     cursor.execute("CREATE DATABASE {}".format(dbname))
#     print("Database Created..")
# except mc.Error as e:
#     print(e)



# Define your database connection parameters
rds_host = 'mstdbinstance.coejywpn3aup.us-east-1.rds.amazonaws.com'
username = 'admins'
password = 'password'
db_name = 'mstdb'
conn = ''
# Connect to the database
try:
    conn = pymysql.connect(
        host=rds_host,
        user=username,
        password=password,
        database=db_name,
        port=3306,
        connect_timeout=30  # Increase timeout to 30 seconds
    )
    print("Connection established successfully.")
except pymysql.MySQLError as e:
    print(f"ERROR: Could not connect to MySQL instance. {e}")
finally:
    if conn:
        conn.close()
        print("Connection closed.")
