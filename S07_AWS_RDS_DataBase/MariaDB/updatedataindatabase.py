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
    cur.execute("UPDATE Persion SET name ='mst' where id =1")
    db.commit()
    print('data updated ..')
    
except mariadb.Error as e:
    print(e)
finally:
    if db:
        db.close()
        print("Database connection close..")
    