import hashlib
import mysql.connector
import datetime

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="agriculturedatabase"
)
cursor = conn.cursor()

# Function to create a hash of a block
def hash_block(index, timestamp, transactions, proof, previous_hash):
    block_string = f"{index}{timestamp}{transactions}{proof}{previous_hash}".encode()
    return hashlib.sha256(block_string).hexdigest()

# Function to add a new block to the database
def add_block(index, transactions, proof, previous_hash):
    timestamp = datetime.datetime.now()
    block_hash = hash_block(index, timestamp, transactions, proof, previous_hash)

    query = """
    INSERT INTO blockchain (index_no, timestamp, transactions, proof, previous_hash)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (index, timestamp, transactions, proof, previous_hash)

    cursor.execute(query, values)
    conn.commit()
    print(f"Block {index} added to database!")

# Fetch the last block
cursor.execute("SELECT * FROM blockchain ORDER BY id DESC LIMIT 1;")
last_block = cursor.fetchone()

if last_block:
    last_index = last_block[1]
    last_hash = hash_block(*last_block)
else:
    last_index = 0
    last_hash = "0000000000000000"

# Add a new block
add_block(last_index + 1, "Sample Blockchain Transaction", 1001, last_hash)

conn.close()
