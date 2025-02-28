import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="agriculturedatabase"
)

cursor = conn.cursor()

# Insert a sample blockchain record
query = """
INSERT INTO blockchain (index_no, timestamp, transactions, proof, previous_hash)
VALUES (%s, NOW(), %s, %s, %s)
"""
values = (1, "Sample Transaction Data", 12345, "000000000000")

cursor.execute(query, values)
conn.commit()  # Save changes

print("Data inserted successfully!")

conn.close()
