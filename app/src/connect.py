import psycopg2  # type: ignore


def connect():
    try:
        with psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="password",
            host="db",
            port="5432"
        ) as conn:
            print("Connected to database")
            return conn
    except psycopg2.DatabaseError as e:
        print(f"Error {e}")
