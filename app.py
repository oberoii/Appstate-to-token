from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    appstate = data.get("appstate", "")

    if not appstate:
        return jsonify({"error": "Appstate is required"}), 400

    # ❗ MOCK conversion (for learning only)
    fake_token = "EAAD_FAKE_TOKEN_" + str(len(appstate))

    return jsonify({
        "token": fake_token,
        "status": "success"
    })

if __name__ == "__main__":
    app.run()
