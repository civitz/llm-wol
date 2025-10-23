import requests
from flask import Flask, request, Response, render_template
import subprocess
import time
import yaml
import hashlib
import base64

app = Flask(__name__)

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

BACKEND_HOST = config['backend']['host']
BACKEND_URL_VERIFY = config['backend']['verifyUrl']
SHUTDOWN_SCRIPT = config['script']['shutdown']
START_SCRIPT = config['script']['start']
STOP_SCRIPT = config['script']['stop']
PASSWORD = config['backend']['password']
SERVICE_PASSWORD = config['service']['password']
SERVICE_SALT = config['service']['salt']
SERVICE_PORT = config['service']['port']
SERVICE_LINK = config['service']['link']

def verify_password(input_password, stored_hash, salt):
    # Decode the base64 salt
    salt_bytes = base64.b64decode(salt)
    
    # Create the hash using PBKDF2 with 600000 iterations
    password_bytes = input_password.encode('utf-8')
    hashed = hashlib.pbkdf2_hmac('sha256', password_bytes, salt_bytes, 600000)
    
    # Encode the result as base64 for comparison
    hashed_b64 = base64.b64encode(hashed).decode('utf-8')
    
    # Compare with stored hash
    return hashed_b64 == stored_hash

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    try:
        # Check if backend is reachable
        response = requests.get(BACKEND_URL_VERIFY, timeout=5)
        if response.status_code == 200:
            app.logger.info("backend is up")
            return render_status_page("Up")
        else:
            app.logger.info("backend is down")
            # Backend is not reachable, show status page
            return render_status_page("Down")
    except requests.exceptions.RequestException as e:
        app.logger.info("backend is down", e)
        # Backend is not reachable, show status page
        return render_status_page("Down")

def render_status_page(status):
    app.logger.info("rendering statuspage")
    return render_template("status.html", status=status, service_link=SERVICE_LINK)



@app.route('/start', methods=['POST'])
def start_backend():
    app.logger.info("start backend?")
    password = request.form.get('password')

    if not verify_password(password, SERVICE_PASSWORD, SERVICE_SALT):
        app.logger.warn("invalid password")
        return render_template("start.html", success=False, service_link=SERVICE_LINK, error_message="Invalid password"), 401

    try:
        # Run the start script
        subprocess.run([START_SCRIPT], check=True)

        # Redirect to main page
        return render_template("start.html", success=True, service_link=SERVICE_LINK), 200
    except Exception as e:
        return render_template("start.html", success=False, service_link=SERVICE_LINK, error_message=f"Error: {e}"), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=SERVICE_PORT, debug=True)
