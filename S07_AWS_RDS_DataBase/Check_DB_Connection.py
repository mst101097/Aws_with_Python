import mysql.connector as mc

try:
    mydb= mc.connect(
        host="",
        user="",
        password=""
    )
    print("Connect establish")

except mc.Error as e:
    print(f'There is not connection establish {e}')
