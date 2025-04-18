todo_list = [
    {"task": "파이썬 공부하기", "done": False},
    {"task": "운동하기", "done": True}
]

def addTodo():
    todo = input("할 일을 입력하세요: ").strip()
    if todo == "":
        print("⚠️ 공백은 입력할 수 없어요!")
    todo_list.append({"task": todo, "done": False})

def SeeList():
    if len(todo_list) == 0:
        print("할 일이 없습니다!")
    else:
        sorted_list = sorted(todo_list, key=lambda x: x["done"])
    
        for number, value in enumerate(sorted_list, start=1):
            icon = "✅" if value["done"] else "⏳"
            print(f"[{number}] {icon} {value['task']}")

def complete():
    number = int(input("몇 번 항목을 완료로 표시할까요? "))-1
    if 0 <= number < len(todo_list):
        todo_list[number]["done"] = True
        print("✅ '%s' 항목이 완료 처리되었습니다!" % todo_list[number]["task"])
    else:
        print("❌ 존재하지 않는 번호예요.")

while True:
    # 메뉴 출력
    print("\n📋 나의 할 일 관리 프로그램\n----------------------------")
    print("1. 할 일 추가")
    print("2. 전체 할 일 보기")  
    print("3. 완료 표시")        
    print("0. 종료")
    
    choice = input("메뉴 선택: ")

    if choice == "1":
        addTodo()
    elif choice == "2":
        SeeList()
    elif choice == "3":
        complete()
    elif choice == "0":
        break
    else:
        print("❌ 잘못된 입력입니다.")