import os
import mysql.connector
"""Module for MySQL connection"""


def connection():
    """MySQL connection parameters
    """
    password = os.getenv("password")
    user = os.getenv("user")

    conn = mysql.connector.connect(
        host='localhost',
        user=user,
        password=password,
        database='agrofoods'
    )

    return conn
