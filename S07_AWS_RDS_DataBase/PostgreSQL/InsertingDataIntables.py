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

    query = "INSERT INTO Employee(ID, NAME, EMAIL) VALUES (1,'MOHIT','MOHIT@GAMIL.COM')"
    query = "INSERT INTO Employee(ID, NAME, EMAIL) VALUES (2,'rohit','rohit@GAMIL.COM')"

    mycursor.execute(query)

    conn.commit()
    print("Data inserted..")
except:
    print("Can't create the table ..")