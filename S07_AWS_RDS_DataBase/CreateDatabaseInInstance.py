import mysql.connector as mc

try:
    mydb = mc.connect(
        host="",
        user="",
        password=""
    )

    dbname = input("Please enter your database.")

    cursor = mydb.cursor()

    cursor.execute("CREATE DATABASE {}".format(dbname))
    print("Database Created..")
except mc.Error as e:
    print(e)