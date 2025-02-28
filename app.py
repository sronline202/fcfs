from flask import Flask, jsonify
import datetime
import hashlib
import json
import mysql.connector

app = Flask(__name__)

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=100, previous_hash='0')  # Genesis block

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        self.save_block_to_db(block)
        return block

    def save_block_to_db(self, block):
        db = mysql.connector.connect(host="localhost", user="root", password="", database="agriculturedatabase")
        cursor = db.cursor()
        
        sql = "INSERT INTO blockchain (block_index, timestamp, proof, previous_hash) VALUES (%s, %s, %s, %s)"
        values = (block['index'], block['timestamp'], block['proof'], block['previous_hash'])
        
        cursor.execute(sql, values)
        db.commit()
        cursor.close()
        db.close()

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1
        return new_proof

blockchain = Blockchain()

@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = hashlib.sha256(json.dumps(previous_block, sort_keys=True).encode()).hexdigest()
    block = blockchain.create_block(proof, previous_hash)
    
    response = {
        'message': 'Block mined successfully!',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200

@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
