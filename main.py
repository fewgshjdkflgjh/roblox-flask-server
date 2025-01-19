from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to receive messages
@app.route('/receive-message', methods=['POST'])
def receive_message():
    data = request.json  # Parse JSON payload
    message = data.get('message', '')

    if message:
        print(f"Received message: {message}")
        return jsonify({"status": "success", "message": message}), 200
    else:
        return jsonify({"status": "error", "message": "No message received"}), 400

# Endpoint to test the server
@app.route('/')
def home():
    return "Server is running!", 200

# Start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
