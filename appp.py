from flask import Flask, jsonify
from web3 import Web3

app = Flask(__name__)

# Connect to Local Blockchain (e.g., Ganache)
blockchain_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(blockchain_url))

# Check if connected
if web3.is_connected():
    print("Connected to Blockchain")

@app.route('/')
def index():
    return "Blockchain Integration with Flask!"

@app.route('/blockNumber')
def block_number():
    latest_block = web3.eth.block_number
    return jsonify({"latest_block": latest_block})

if __name__ == '__main__':
    app.run(port=5000)
