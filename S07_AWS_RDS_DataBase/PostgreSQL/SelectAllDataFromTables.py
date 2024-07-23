import psycopg2

try:
    conn = psycopg2.connect(
        database ="",
        user ="",
        password="",
        host ="",
        port= 5432)

    conn.autocommit = True

    mycursor = conn.cursor()

    query = "SELECT * FORM Employee"

    mycursor.execute(query)
    
    for data in mycursor.fetchall():
        print(data)

except:
    print("Can't connect the database ..")