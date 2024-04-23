import mysql.connector

# Establishing a connection to the MySQL database
try:
    # Replace 'host', 'user', 'password', and 'database' with your MySQL server details
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="MySQL123.com",
        database="task_management"
    )
    
    if connection.is_connected():
        print("Connected to MySQL database")
        
        # Perform database operations here
        
except mysql.connector.Error as error:
    print("Error connecting to MySQL database:", error)

finally:
    # Closing the database connection
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL database connection closed")
