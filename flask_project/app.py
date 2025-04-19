from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todo_list = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form["username"]
    todo_list.append(username)
    return redirect(url_for("show_list"))

@app.route("/list")
def show_list():
    return render_template("list.html", items=todo_list)

@app.route("/delete/<int:item_id>", methods=["POST"])
def delete(item_id):
    if 0 <= item_id < len(todo_list):
        todo_list.pop(item_id)
    return redirect(url_for("show_list"))


if __name__ == "__main__":
    app.run(debug=True)
