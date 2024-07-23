import mariadb

try:
    db = mariadb.connect(
        host="mariadbinstance.coejywpn3aup.us-east-1.rds.amazonaws.com",
        user ="admin",
        password="password"
    )

    dbname = input("Please enter the DB name: ")
    cur = db.cursor()
    cur.execute("CREATE DATABASE {}".format(dbname))
    
    print('Database Created..')
except mariadb.Error as e:
    print(e)
    