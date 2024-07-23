import mariadb

try:
    db = mariadb.connect(
        host="mariadbinstance.coejywpn3aup.us-east-1.rds.amazonaws.com",
        user ="admin",
        password="password",
        database = "mydb"
    )
    print('Database Connection Eastablish..')

except mariadb.Error as e:
    print(e)
finally:
    if db:
        db.close()
        print("Connection close..")