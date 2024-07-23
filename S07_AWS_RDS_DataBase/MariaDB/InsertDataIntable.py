import mariadb

try:
    db = mariadb.connect(
        host="mariadbinstance.coejywpn3aup.us-east-1.rds.amazonaws.com",
        user ="admin",
        password="password",
        database = "mydb"
    )

    cur = db.cursor()
    
    # cur.execute("INSERT INTO Persion (id,name,email) VALUES(1,'MOHIT','EMAIL.COM')")
    cur.execute("INSERT INTO Persion (id,name,email) VALUES(2,'rohit','rohitemail.com')")
    db.commit()
    print('DATA INSERTED....')
except mariadb.Error as e:
    print(e)
finally:
    if db:
        db.close()
        print("Database connection close..")
    