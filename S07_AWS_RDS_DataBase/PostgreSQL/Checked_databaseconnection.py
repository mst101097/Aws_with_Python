import psycopg2

try:
    conn = psycopg2.connect(
        database ="",
        user ="",
        password="",
        host ="",
        port= 5432
    )

    print("database connected.. ")
except:
    print("Faild to connect the database")