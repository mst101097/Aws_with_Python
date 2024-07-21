import mysql.connector as mc

try:
    mydb= mc.connect(
        host="",
        user="",
        password="",
        database=""
    )

    mycursor = my.cursor()

    mycursor.execute(
        "Create Table Person( id int AUTO_INCREMENT PRIMERY KEY,name varchar(266),last_name  varchar(266)")
    
    print("Table created")

except mc.Error as e:
    print(f"Table not Created {e}")
    