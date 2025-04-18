import json
from datetime import datetime
TODO_FILE = "todo_data.json"
show_completed = False  # 기본값: 완료 항목 숨기기

todo_list = [
    {
        "task": "파이썬 과제 제출하기",
        "done": False,
        "due": "2025-04-20",
        "priority": 1
    },
    {
        "task": "헬스장 가기",
        "done": True,
        "due": "2025-04-18",
        "priority": 3
    },
    {
        "task": "책 30쪽 읽기",
        "done": False,
        "due": "2025-04-22",
        "priority": 2
    }
]


#할 일 추가
def addTodo():
    todo = input("할 일을 입력하세요: ").strip()
    if todo == "":
        print("⚠️ 공백은 입력할 수 없어요!")
    else:
        try:            
            date = input("날짜를 입력하세요 (예: 2025-04-02): ")
            datetime.strptime(date, "%Y-%m-%d")

            number = getNumberInput("이 할 일 얼마나 중요해요? (1: ⭐ 꼭 해야 해 / 2: 🙂 해두면 좋아 / 3: 😌 여유 있어)")
            if 0 < number <= 3:
                todo_list.append({"task": todo, "done": False, "due": date, "priority": number})
                print("✅ 할 일이 추가되었습니다!")
            else:
                print("⚠️ 우선순위 설정이 잘못되었습니다. 다시 시도해주세요.")
        except ValueError:
            print("⚠️ 날짜 형식이 잘못되었습니다. 다시 입력해주세요.")

#전체 할 일 보기
def SeeList():
    if len(todo_list) == 0:
        print("할 일이 없습니다!")
    else:
        sorted_list = sorted(todo_list, key=lambda x: x["priority"])
        count = 0
    
        for number, value in enumerate(sorted_list, start=1):
            if not show_completed and value["done"]:
                continue  # ✅ 완료 항목은 건너뜀

            icon = "✅" if value["done"] else "⏳"
            if value['priority'] == 1:
                print(f"[{number}] {icon} {value['task']} (마감: {value['due']}, ⭐ 우선순위: 높음)")
            elif value['priority'] == 2:
                print(f"[{number}] {icon} {value['task']} (마감: {value['due']}, 🙂 우선순위: 보통)")
            else:
                print(f"[{number}] {icon} {value['task']} (마감: {value['due']}, 😌 우선순위: 낮음))")
            count += 1
    print(f"----------------------------\n총 {count}개의 할 일을 표시 중입니다.")

#완료 표시
def complete():
    number = getNumberInput("몇 번 항목을 완료로 표시할까요? ")
    if number is not None and 0 <= number < len(todo_list):
        todo_list[number]["done"] = True
        print("✅ '%s' 항목이 완료 처리되었습니다!" % todo_list[number]["task"])
    elif number is not None:
        print("❌ 존재하지 않는 번호예요.")

#항목 삭제 
def delTodo():
    number = getNumberInput("몇 번 항목을 삭제할까요? ")
    if number is not None and 0 <= number < len(todo_list):
        print("🗑️ '%s' 항목이 삭제되었습니다!" % todo_list[number]["task"])
        del todo_list[number]
    elif number is not None:
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

# 메뉴 출력 함수
def printMenu():
    print("\n📋 나의 할 일 관리 프로그램\n----------------------------")
    print("1. 할 일 추가")
    print("2. 전체 할 일 보기")  
    print("3. 완료 표시")     
    print("4. 항목 삭제")   
    print("5. 저장하기")
    print("6. 불러오기")
    print("7. 완료된 항목 보기 ON/OFF")
    print("0. 종료")

# 번호 입력 받는 함수 (예외처리 포함)
def getNumberInput(prompt):
    try:
        return int(input(prompt)) - 1
    except ValueError:
        print("❌ 숫자만 입력해 주세요!")
        return None

def toggleCompletedView():
    global show_completed
    show_completed = not show_completed
    state = "ON" if show_completed else "OFF"
    print(f"✅ 완료 항목 보기: {state}")

while True:
    printMenu()
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
    elif choice == "7":
        toggleCompletedView()
    elif choice == "0":
        confirm = input("저장하고 종료할까요? (y/n): ")
        if confirm.lower() == 'y':
            saveTodo()
            print("📕 프로그램을 종료합니다.")
        break
    else:
        print("❌ 잘못된 입력입니다.")