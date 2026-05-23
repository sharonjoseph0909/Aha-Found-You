from flask import Flask, render_template, request, jsonify
import voice_recognition

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("foundyou.html")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    return f"You searched for: {query}"

if __name__ == "__main__":
    app.run(debug=True)