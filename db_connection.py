# db_connection.py
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="product_management_db"
    )
