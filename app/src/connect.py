import psycopg2  # type: ignore


def get_conn():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="password",
            host="db",
            port="5432"
        )
        print("Connected to database")
        yield conn
    except psycopg2.DatabaseError as e:
        print(f"Error {e}")
    finally:
        conn.close()
