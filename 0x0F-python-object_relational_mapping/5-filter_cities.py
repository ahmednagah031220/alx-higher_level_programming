#!/usr/bin/python3
"""
Module used in the task
"""
from sys import argv
import MySQLdb


def main():
    """
    Function used in the task
    """
    db_user = argv[1]
    db_password = argv[2]
    db_db = argv[3]
    db_host = "localhost"
    db_port = 3306
    stateName = argv[4]

    queries = """SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC"""
    connection = MySQLdb.connect(host=db_host, port=db_port,
                                 user=db_user, passwd=db_password,
                                 db=db_db, charset="utf8")
    cursor = connection.cursor()
    cursor.execute(queries, (stateName, ))
    query_rows = cursor.fetchall()
    list_result = []
    for row in query_rows:
        list_result.append(row[0])
    print(", ".join(list_result))
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
