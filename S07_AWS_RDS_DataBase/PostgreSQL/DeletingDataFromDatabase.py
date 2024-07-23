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
    query = "DELETE FROM Employee WHERE id = 1"
    mycursor.execute(query)
    conn.commit()

    print("data deleted..")

except:
    print("Can't connect the database ..")