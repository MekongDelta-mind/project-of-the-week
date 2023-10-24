from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({"message": "Kudos You are accessing the API as a GET request !!"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
