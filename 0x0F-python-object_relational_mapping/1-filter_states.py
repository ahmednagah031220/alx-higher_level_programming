#!/usr/bin/python3
"""
Module used in the task
"""
from sys import argv
import MySQLdb


def main():
    """
    Function of the models
    """
    db_user = argv[1]
    db_password = argv[2]
    db_db = argv[3]
    db_host = "localhost"
    db_port = 3306

    try:
        query_string = "SELECT * FROM states WHERE CONVERT(name USING Latin1)"
        query_string += " COLLATE Latin1_General_CS"
        query_string += " LIKE 'N%'"
        connection = MySQLdb.connect(host=db_host,
                                     port=db_port,
                                     user=db_user,
                                     passwd=db_password,
                                     db=db_db,
                                     charset="utf8")
        try:
            cursor = connection.cursor()
            cursor.execute(query_string)
            query_rows = cursor.fetchall()
            for row in query_rows:
                print(row)
        finally:
            cursor.close()
    finally:
        connection.close()


if __name__ == "__main__":
    main()
