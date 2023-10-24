from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({"message": "Kudos You are accessing the API as a GET request !!"})


if __name__ == "__main__":
    app.run(debug=True) # the default port is 5000. It can be chanegd to anything else
