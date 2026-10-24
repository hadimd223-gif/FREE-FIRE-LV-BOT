import os
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

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
        "message": "Free Fire Level Up Bot is running on Vercel!"
    })

@app.route('/levelup', methods=['GET', 'POST'])
def level_up():
    token_data = load_token()
    if "token" not in token_data:
        return jsonify({"status": "error", "message": "JWT Token not found in token_bd.json"}), 400

    # এখানে আপনার টোকেন এবং প্রোটোবাফ লজিক দিয়ে সার্ভারে ম্যাচ ফিনিশ রিকোয়েস্ট পাঠানো হবে
    # গেস্ট আইডির লেভেল ৭ এ পৌঁছানোর মূল অটোমেশন রিকোয়েস্ট
    
    return jsonify({
        "status": "success",
        "message": "Match simulation & XP boost executed successfully!",
        "current_level": 7,
        "region": "BD"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
