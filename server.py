from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
MEMORY_PATH = "memory.json"

@app.route("/memory", methods=["GET"])
def get_memory():
    if not os.path.exists(MEMORY_PATH):
        return jsonify({})
    with open(MEMORY_PATH, encoding="utf-8") as f:
        return jsonify(json.load(f))

@app.route("/memory", methods=["POST"])
def save_memory():
    data = request.json
    with open(MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return jsonify({"status": "ok", "message": "Memory updated."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
