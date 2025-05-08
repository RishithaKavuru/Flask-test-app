from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        message = f"Hello, {name}!"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            return render_template("index.html", message=f"Hello, {name}!")
        else:
            return render_template("index.html", message="Please enter your name.")
    return render_template("index.html", message="")

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)