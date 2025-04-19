from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todo_list, f, ensure_ascii=False, indent=2)

def load_data():
    global todo_list
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                todo_list = json.load(f)
        except json.JSONDecodeError:
            todo_list = []

todo_list = []
load_data()  # 앱 시작할 때 데이터 불러오기

# --- 라우팅들 ---
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
    save_data()
    return redirect(url_for("show_list"))

@app.route("/list")
def show_list():
    return render_template("list.html", items=todo_list)

@app.route("/delete/<int:item_id>", methods=["POST"])
def delete(item_id):
    if 0 <= item_id < len(todo_list):
        todo_list.pop(item_id)
        save_data()
    return redirect(url_for("show_list"))

if __name__ == "__main__":
    app.run(debug=True)
