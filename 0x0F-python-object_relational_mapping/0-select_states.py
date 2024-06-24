#!/usr/bin/python3
"""
Models used in the task
"""
from sys import argv
import MySQLdb


def main():
    """
    the main function for the porcess
    """
    db_user = argv[1]
    db_password = argv[2]
    db_db = argv[3]
    db_host = "localhost"
    db_port = 3306

    try:
        conn = MySQLdb.connect(host=db_host, port=db_port,
                               user=db_user, passwd=db_password,
                               db=db_db, charset="utf8")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
        query_rows = cursor.fetchall()
        for row in query_rows:
            print(row)
        cursor.close()
        conn.close()
    except Exception:
        pass


if __name__ == "__main__":
    main()
