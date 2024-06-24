#!/usr/bin/python3
"""
Module of the task
"""
from sys import argv
import MySQLdb


def main():
    """
    Function of the task
    """
    db_user = argv[1]
    db_password = argv[2]
    db_db = argv[3]
    db_host = "localhost"
    db_port = 3306

    try:
        queries = "SELECT cities.id, cities.name, states.name "
        queries += "FROM cities LEFT JOIN states "
        queries += "ON cities.state_id=states.id "
        queries += "ORDER BY cities.id ASC"
        connections = MySQLdb.connect(host=db_host, port=db_port,
                                      user=db_user, passwd=db_password,
                                      db=db_db, charset="utf8")
        cursor = connections.cursor()
        cursor.execute(queries)
        query_rows = cursor.fetchall()
        for row in query_rows:
            print(row)
        cursor.close()
        connections.close()
    except Exception:
        pass


if __name__ == "__main__":
    main()
