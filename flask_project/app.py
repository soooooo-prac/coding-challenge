from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form["username"]
    return f"<h2>{username}님, 환영합니다!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
