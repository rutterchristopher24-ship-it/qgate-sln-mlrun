
import os
from auth.admin_manager import AdminLedger
# Assuming a simple Flask setup for the prototype logic
# If this was originally just a script, we wrap it to serve the web interface
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='frontend')
ledger = AdminLedger()

@app.route('/')
def home():
    """Serves the Sign-Up Page"""
    return send_from_directory('frontend', 'signup.html')

@app.route('/api/signup', methods=['POST'])
def signup():
    """Handles the email submission"""
    data = request.form
    email = data.get('email')
    
    if not email:
        return jsonify({"error": "Email is required"}), 400
        
    # Register in the secure Admin Ledger
    ledger.register_user(email)
    
    return jsonify({"message": "Access requested successfully", "status": "pending"})

if __name__ == "__main__":
    # Standard entry point
    print("Launching QGate Interface...")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
