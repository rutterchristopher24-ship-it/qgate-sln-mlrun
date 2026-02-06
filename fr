import os
from auth.admin_manager import AdminLedger
from flask import Flask, request, jsonify, send_from_directory, redirect, url_for

app = Flask(__name__, static_folder='frontend')
ledger = AdminLedger()

@app.route('/')
def home():
    """Serves the Sign-Up Page"""
    return send_from_directory('frontend', 'signup.html')

@app.route('/thank-you')
def thank_you():
    """Serves the Thank You page after signup"""
    return send_from_directory('frontend', 'thank-you.html')

@app.route('/api/signup', methods=['POST'])
def signup():
    """Handles the email submission"""
    data = request.form
    email = data.get('email')
    
    if not email:
        return jsonify({"error": "Email is required"}), 400
        
    # Register in the secure Admin Ledger
    ledger.register_user(email)
    
    # NEW: Move the visitor to the next destination
    return redirect(url_for('thank_you'))

if __name__ == "__main__":
    print("Launching QGate Interface...")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

