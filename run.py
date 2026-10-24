import os
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# টোকেন লোড করার ফাংশন
def load_token():
    token_path = "token_bd.json"
    if os.path.exists(token_path):
        with open(token_path, "r") as f:
            return json.load(f)
    return {"status": "error", "message": "token_bd.json not found"}

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "online",
        "region": "BD",
        "message": "Free Fire API is running successfully on Vercel!"
    })

@app.route('/like', methods=['GET', 'POST'])
def handle_like():
    # ভার্সেল বা লোকাল টেস্টের জন্য GET এবং POST উভয় মেথড রাখা হলো
    if request.method == 'POST':
        data = request.get_json() or {}
        uid = data.get("uid")
    else:
        uid = request.args.get("uid")
    
    server_name = request.args.get("server_name", "BD")

    if not uid:
        return jsonify({"status": "error", "message": "UID is required"}), 400

    token_data = load_token()
    
    # এখানে রিমোট সার্ভার রিকোয়েস্ট হ্যান্ডেল হবে
    print(f"[*] Processing Request for UID: {uid} in Region: {server_name}")

    return jsonify({
        "status": "success",
        "message": f"Successfully processed for UID: {uid}",
        "region": server_name,
        "token_status": "Loaded"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
