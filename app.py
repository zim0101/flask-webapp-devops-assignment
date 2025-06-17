from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)


def get_vm_hostname():
    return os.environ.get('VM_HOSTNAME', socket.gethostname())

def get_commit_hash():
    return os.environ.get('COMMIT_HASH', 'unknown')


@app.route('/')
def home():
    return jsonify({
        "message": "DevOps Problem 1 - v1.0",
        "vm_hostname": get_vm_hostname(),
        "commit_hash": get_commit_hash(),
    })


@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)
