import psycopg2
from psycopg2._psycopg import OperationalError

def create_connection():
    try:
        conn = psycopg2.connect(
            # Sanatized for Git
        )
        return conn
    except OperationalError as e:
        print(f"{e}")
        return conn


connection =create_connection()
