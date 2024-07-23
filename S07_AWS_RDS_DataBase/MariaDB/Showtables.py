import mariadb

try:
    db = mariadb.connect(
        host="mariadbinstance.coejywpn3aup.us-east-1.rds.amazonaws.com",
        user ="admin",
        password="password",
        database = "mydb"
    )

    cur = db.cursor()
    
    cur.execute("SHOW TABLES")
    for data in cur.fetchall():
        print(data)

except mariadb.Error as e:
    print(e)
finally:
    if db:
        db.close()
        print("Database connection close..")
    