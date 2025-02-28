from flask import Flask, jsonify, request
import datetime
import hashlib
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof=1, previous_hash='0000')  # Genesis Block

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'transactions': self.transactions,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.transactions = []  # Reset transactions
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        while True:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':  # Simple Proof-of-Work condition
                return new_proof
            new_proof += 1

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def add_transaction(self, transaction_data):
        self.transactions.append(transaction_data)
        return self.get_previous_block()['index'] + 1  # Returns next block index

# Initialize Flask App
app = Flask(__name__)
blockchain = Blockchain()

# Route 1: Get Full Blockchain
@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    response = {'chain': blockchain.chain, 'length': len(blockchain.chain)}
    return jsonify(response), 200

# Route 2: Add a New Transaction
@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    data = request.get_json()
    if 'transactions' not in data:
        return jsonify({'message': 'Invalid transaction data'}), 400
    
    index = blockchain.add_transaction(data['transactions'])
    return jsonify({'message': f'Transaction added to block {index}'}), 201

# Route 3: Mine a Block
@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    
    block = blockchain.create_block(proof, previous_hash)
    return jsonify(block), 201

# Run Flask App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
