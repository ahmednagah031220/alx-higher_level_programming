#!/usr/bin/python3
"""
Module Docs
"""
from sys import argv
import MySQLdb


def main():
    """
    Function to use in the task
    """
    db_user = argv[1]
    db_password = argv[2]
    db_db = argv[3]
    db_host = "localhost"
    db_port = 3306
    string_to_share = argv[4]

    try:
        query_string = "SELECT id, name FROM states WHERE "
        query_string += "name=%s ORDER BY id ASC"
        connection = MySQLdb.connect(host=db_host, port=db_port,
                                     user=db_user, passwd=db_password,
                                     db=db_db, charset="utf8")
        try:
            cursor = connection.cursor()
            cursor.execute(query_string, (string_to_share, ))
            query_rows = cursor.fetchall()
            for row in query_rows:
                print(row)
        finally:
            cursor.close()
    finally:
        connection.close()


if __name__ == "__main__":
    main()
