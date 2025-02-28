from flask import Flask, jsonify, request
import mysql.connector
import datetime
import hashlib
import json
import jwt

# Flask app setup
app = Flask(__name__)

# Secret key for authentication
SECRET_KEY = "supersecret"

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="blockchain_db"
)
cursor = db.cursor()

# Create blockchain table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS blockchain (
        id INT AUTO_INCREMENT PRIMARY KEY,
        index_no INT UNIQUE,
        previous_hash TEXT,
        proof INT,
        timestamp TEXT,
        transactions TEXT
    )
""")
db.commit()

# Function to compute hash of a block
def compute_hash(block):
    block_string = json.dumps(block, sort_keys=True)
    return hashlib.sha256(block_string.encode()).hexdigest()

# Function to get the last block
def get_last_block():
    cursor.execute("SELECT * FROM blockchain ORDER BY index_no DESC LIMIT 1")
    last_block = cursor.fetchone()
    if last_block:
        return {
            "index_no": last_block[1],
            "previous_hash": last_block[2],
            "proof": last_block[3],
            "timestamp": last_block[4],
            "transactions": last_block[5]
        }
    return None  # No blocks exist (Genesis Block case)

# Function to create the Genesis Block
def create_genesis_block():
    cursor.execute("SELECT COUNT(*) FROM blockchain")
    count = cursor.fetchone()[0]

    if count == 0:  # If no blocks exist, create Genesis Block
        genesis_block = {
            "index_no": 1,
            "previous_hash": "0000",
            "proof": 100,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "transactions": "Genesis Block"
        }
        cursor.execute("""
            INSERT INTO blockchain (index_no, previous_hash, proof, timestamp, transactions) 
            VALUES (%s, %s, %s, %s, %s)
        """, (genesis_block["index_no"], genesis_block["previous_hash"], genesis_block["proof"], genesis_block["timestamp"], genesis_block["transactions"]))
        db.commit()

# Function to generate proof-of-work
def proof_of_work(previous_proof):
    new_proof = 1
    while True:
        hash_value = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
        if hash_value[:4] == "0000":  # Valid proof if first 4 chars are "0000"
            return new_proof
        new_proof += 1

# Call Genesis Block creation at app startup
create_genesis_block()

# 🏠 Home Route
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Blockchain API is running! Use /blockchain, /add_transaction, /mine_block'}), 200

# 📜 Get Full Blockchain
@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    cursor.execute("SELECT * FROM blockchain ORDER BY index_no ASC")
    blocks = cursor.fetchall()
    blockchain = [
        {"id": row[0], "index_no": row[1], "previous_hash": row[2], "proof": row[3], "timestamp": row[4], "transactions": row[5]}
        for row in blocks
    ]
    return jsonify({"length": len(blockchain), "chain": blockchain}), 200

# 🔐 Generate API Token for Authentication
@app.route('/generate_token', methods=['POST'])
def generate_token():
    payload = {"exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return jsonify({"token": token})

# 📝 Add a Transaction (Requires Token)
@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"message": "Missing token!"}), 401

    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token expired!"}), 403
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token!"}), 403

    data = request.get_json()
    if not data or 'transactions' not in data:
        return jsonify({'message': 'Invalid transaction data'}), 400

    last_block = get_last_block()
    previous_hash = "0000" if not last_block else compute_hash(last_block)
    index_no = 1 if not last_block else last_block["index_no"] + 1
    proof = (last_block["proof"] + 100) if last_block else 100
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO blockchain (index_no, previous_hash, proof, timestamp, transactions) 
        VALUES (%s, %s, %s, %s, %s)
    """, (index_no, previous_hash, proof, timestamp, data['transactions']))
    db.commit()

    return jsonify({'message': 'Transaction added', 'block_index': index_no}), 201

# ⛏️ Mine a New Block
@app.route('/mine_block', methods=['GET'])
def mine_block():
    last_block = get_last_block()
    if not last_block:
        return jsonify({'message': 'No transactions to mine. Add a transaction first!'}), 400

    previous_proof = last_block["proof"]
    proof = proof_of_work(previous_proof)
    previous_hash = compute_hash(last_block)
    index_no = last_block["index_no"] + 1
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO blockchain (index_no, previous_hash, proof, timestamp, transactions) 
        VALUES (%s, %s, %s, %s, %s)
    """, (index_no, previous_hash, proof, timestamp, "[]"))
    db.commit()

    return jsonify({'message': 'New block mined!', 'index_no': index_no, 'proof': proof, 'previous_hash': previous_hash}), 201

# ✅ Validate Blockchain Integrity
@app.route('/validate_chain', methods=['GET'])
def validate_chain():
    cursor.execute("SELECT * FROM blockchain ORDER BY index_no ASC")
    blocks = cursor.fetchall()

    previous_hash = "0000"
    for block in blocks:
        block_data = {
            "index_no": block[1],
            "previous_hash": block[2],
            "proof": block[3],
            "timestamp": block[4],
            "transactions": block[5]
        }
        calculated_hash = compute_hash(block_data)

        if previous_hash != block[2]:  # Validate hash link
            return jsonify({"message": "Blockchain is INVALID!"}), 400

        previous_hash = calculated_hash  # Move to next block

    return jsonify({"message": "Blockchain is VALID!"}), 200

# Start Flask App
if __name__ == '__main__':
    app.run(debug=True, port=5000)
