import mysql.connector
"""Module for MySQL connection"""


def connection():
    """MySQL connection parameters
    """

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Betini2024',
        database='agrofoods'
    )

    return conn
