import sqlite3
from sqlite3 import Error


def connect(db_file):
    try:
        connection = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error:
        print(Error)
    finally:
        connection.close()


if __name__ == "__main__":
    connect("database.db")
