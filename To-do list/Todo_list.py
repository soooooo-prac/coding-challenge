import json
import datetime
TODO_FILE = "todo_data.json"

todo_list = [
    {"task": "파이썬 공부하기", "done": False},
    {"task": "운동하기", "done": True}
]

#할 일 추가
def addTodo():
    todo = input("할 일을 입력하세요: ").strip()
    if todo == "":
        print("⚠️ 공백은 입력할 수 없어요!")
    todo_list.append({"task": todo, "done": False})

#전체 할 일 보기
def SeeList():
    if len(todo_list) == 0:
        print("할 일이 없습니다!")
    else:
        sorted_list = sorted(todo_list, key=lambda x: x["done"])
    
        for number, value in enumerate(sorted_list, start=1):
            icon = "✅" if value["done"] else "⏳"
            print(f"[{number}] {icon} {value['task']}")

#완료 표시
def complete():
    number = int(input("몇 번 항목을 완료로 표시할까요? "))-1
    if 0 <= number < len(todo_list):
        todo_list[number]["done"] = True
        print("✅ '%s' 항목이 완료 처리되었습니다!" % todo_list[number]["task"])
    else:
        print("❌ 존재하지 않는 번호예요.")

#항목 삭제 
def delTodo():
    number = int(input("몇 번 항목을 삭제할까요? "))-1
    if 0 <= number < len(todo_list):
        print("🗑️ '%s' 항목이 삭제되었습니다!" % todo_list[number]["task"])
        del todo_list[number]
    else:
        print("❌ 존재하지 않는 번호예요.")

#저장하기
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

while True:
    # 메뉴 출력
    print("\n📋 나의 할 일 관리 프로그램\n----------------------------")
    print("1. 할 일 추가")
    print("2. 전체 할 일 보기")  
    print("3. 완료 표시")     
    print("4. 항목 삭제")   
    print("5. 저장하기")
    print("6. 불러오기")
    print("0. 종료")
    
    choice = input("메뉴 선택: ")

    if choice == "1":
        addTodo()
    elif choice == "2":
        SeeList()
    elif choice == "3":
        complete()
    elif choice == "4":
        delTodo()
    elif choice == "5":
        saveTodo()
    elif choice == "6":
        loadTodo()
    elif choice == "0":
        confirm = input("저장하고 종료할까요? (y/n): ")
        if confirm.lower() == 'y':
            saveTodo()
            print("📕 프로그램을 종료합니다.")
        break
    else:
        print("❌ 잘못된 입력입니다.")