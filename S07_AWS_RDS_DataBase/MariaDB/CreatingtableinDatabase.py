import mariadb

try:
    db = mariadb.connect(
        host="mariadbinstance.coejywpn3aup.us-east-1.rds.amazonaws.com",
        user ="admin",
        password="password",
        database = "mydb"
    )

    cur = db.cursor()
    
    cur.execute("CREATE TABLE Persion (id INT NOT NULL, name TEXT,email TEXT)")
    db.commit()
    print('table Created..')
except mariadb.Error as e:
    print(e)
finally:
    if db:
        db.close()
        print("Database connection close..")
    