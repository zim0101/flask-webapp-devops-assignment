from flask import Flask, jsonify
import socket
import os
import subprocess
from datetime import datetime


app = Flask(__name__)


def get_commit_hash():
    return os.environ.get('COMMIT_HASH', 'unknown')

@app.route('/')
def home():
    return jsonify({
        "message": "DevOps Problem 1",
        "vm_hostname": socket.gethostname(),
        "commit_hash": get_commit_hash(),
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "vm_hostname": socket.gethostname(),
        "commit_hash": get_commit_hash()
    })


if __name__ == '__main__':
    print(f"Starting Flask app on:")
    print(f"  VM Hostname: {socket.gethostname()}")
    print(f"  Commit Hash: {get_commit_hash()}")
    
    app.run(host='0.0.0.0', port=3000, debug=False)