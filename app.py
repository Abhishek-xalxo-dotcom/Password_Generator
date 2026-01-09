from flask import Flask, render_template, request, jsonify
from password_gen import generate_password

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    length = int(data.get("length", 20))

    try:
        password = generate_password(length)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({
        "length": length,
        "password": password
    })

if __name__ == "__main__":
    app.run(debug=True)
