import mysql.connector
from mysql.connector import Error

db_config = {
    'user': 'root',
    'password': 'password@123',
    'host': 'localhost',
    'database': 'build'
}

def db_connect():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        return jsonify({"message": str(e)}), 500