import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection to the MySQL server."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="Local_host",
            password="qep3aInwhy(t8SdP",
            database="dissertation_project",
            auth_plugin='mysql_native_password'
        )
        print("Connection to MySQL DB successful")
        return conn
    except Error as e:
        print(f"The error '{e}' occurred")

mydb = create_connection()


#qep3aInwhy(t8SdP