import json
import datetime
TODO_FILE = "todo_data.json"

todo_list = [
    {"task": "파이썬 공부하기", "done": False},
    {"task": "운동하기", "done": True}
]

def saveTodo():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d")
    TODO_FILE = f"todo_{current_time}.json"
    
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todo_list, f, ensure_ascii=False, indent=4)
        print("📁 할 일 목록이 저장되었습니다!")

#불러오기
def loadTodo():
    global todo_list
    try:
        with open("todo_data.json", "r", encoding="utf-8") as f:
            todo_list = json.load(f)
            print("📂 저장된 할 일 목록을 불러왔습니다!")
    except FileNotFoundError:
        print("📂 저장된 파일이 없습니다. 새로 시작합니다.")
        todo_list = []
    except json.JSONDecodeError:
        print("⚠️ 파일 형식이 잘못되었습니다. 새로 시작합니다.")
        todo_list = []
