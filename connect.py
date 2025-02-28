import mysql.connector

# Connect to MySQL Database
conn = mysql.connector.connect(
    host="localhost",   # XAMPP runs MySQL locally
    user="root",        # Default XAMPP MySQL user
    password="",        # Default XAMPP MySQL has no password (leave empty)
    database="agriculturedatabase"  # Your database name
)

# Check if connection is successful
if conn.is_connected():
    print("Connected to MySQL successfully!")

cursor = conn.cursor()

# Test query: Show available tables
cursor.execute("SHOW TABLES;")

print("Tables in database:")
for table in cursor:
    print(table)

# Close the connection
conn.close()
