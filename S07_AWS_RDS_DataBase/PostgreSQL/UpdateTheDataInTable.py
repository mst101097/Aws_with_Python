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
    query = "UPDATE Employee SET NAME ='MST' WHERE ID = 1"
    mycursor.execute(query)
    conn.commit()

    print("DATA UPDATED..")

except:
    print("Can't connect the database ..")