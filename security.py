from flask import Flask
from flask_talisman import Talisman
from flask import CORS

app = Flask(__name__)
Talisman(app)  # Enforces HTTPS

CORS(app, origins=["https://trusted-site.com"])

@app.route('/')
def home():
    return "Secure Flask Service"

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))  # Use SSL/TLS cert
