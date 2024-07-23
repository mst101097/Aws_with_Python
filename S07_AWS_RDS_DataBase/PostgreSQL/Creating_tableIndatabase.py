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

    query = """
        CREATE TABLE Employee(
        ID INT PRIMERY KEY NOT NULL,
        NAME TEXT NOT NULL,
        EMAIL TEXT NOT NULL
        )
    """

    mycursor.execute(query)
    conn.commit()
    print("table createed ..")
except:
    print("Can't create the table ..")