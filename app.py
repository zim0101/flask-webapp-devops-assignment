from flask import Flask, jsonify
import socket
import os
import subprocess
from datetime import datetime


app = Flask(__name__)


def get_vm_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "unknown"

def get_commit_hash():
    commit = os.environ.get('COMMIT_HASH')
    if commit:
        return commit
    
    try:
        result = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return result.stdout.strip()
    except:
        pass
    
    return f"dev-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Flask Web App!",
        "hostname": socket.gethostname(),
        "vm_ip": get_vm_ip(),
        "commit_hash": get_commit_hash(),
        "timestamp": datetime.now().isoformat(),
        "status": "healthy"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "hostname": socket.gethostname(),
        "vm_ip": get_vm_ip()
    })

if __name__ == '__main__':
    print(f"Starting Flask app on {socket.gethostname()}")
    print(f"VM IP: {get_vm_ip()}")
    print(f"Commit Hash: {get_commit_hash()}")
    app.run(host='0.0.0.0', port=3000, debug=False)
