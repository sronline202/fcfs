import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="agriculturedatabase"
)

cursor = conn.cursor()

# Retrieve all blockchain records
cursor.execute("SELECT * FROM blockchain;")
rows = cursor.fetchall()

print("Blockchain Data:")
for row in rows:
    print(row)

conn.close()
