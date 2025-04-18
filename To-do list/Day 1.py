import json

todo_list = []
TODO_FILE = "todo_data.json"

while True:
    print("📋 나의 할 일 관리 프로그램\n----------------------------\n1. 할 일 추가\n0. 종료")
    choice = input("메뉴 선택: ")
    
    if choice == "1":
        todo = input("할 일을 입력하세요: ").strip()
        if todo == "":
            print("⚠️ 공백은 입력할 수 없어요!")
            continue
        todo_list.append({"task": todo, "done": False})
        print("✅ 할 일이 추가되었습니다!")
    elif choice == "0":
        print("👋 프로그램을 종료합니다.")
        break
    else:
        print("❌ 잘못된 입력입니다.")