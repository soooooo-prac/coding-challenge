import json
from datetime import datetime

account_list = []  # 전체 항목 저장
FILE_NAME = "account_book.txt"  # 저장 파일 이름

def main():
    load_data()

    while True:
        print_menu()
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            print_list()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            save_data()
        elif choice == "6":
            load_data()
        elif choice == "0":
            confirm = input("저장하고 종료할까요? (y/n): ")
            if confirm.lower() == 'y':
                save_data()
            print("📕 프로그램을 종료합니다.")
            break
        else:
            print("⚠️ 잘못된 입력입니다. 다시 선택해주세요.")

def print_menu():
    print("\n📒 나의 가계부")
    print("----------------------------")
    print("1. 항목 추가")
    print("2. 목록 보기")
    print("3. 수입/지출 총합 보기")
    print("4. 항목 삭제")
    print("5. 저장하기")
    print("6. 불러오기")
    print("0. 종료")
    print("----------------------------")
    
def add_item():
    # 날짜
    while True:
        try:
            date = input("날짜를 입력하세요 (예: 2025-04-02): ")
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("⚠️ 날짜 형식이 잘못되었습니다. 다시 입력해주세요.")

    # 분류
    while True:
        category = input("분류를 입력하세요 (수입/지출): ")
        if category in ['수입', '지출']:
            break
        else:
            print("⚠️ 분류는 '수입' 또는 '지출'만 가능합니다.")

    # 내용
    content = input("내용을 입력하세요: ")

    # 금액
    while True:
        try:
            amount = int(input("금액을 입력하세요: "))
            if amount < 0:
                print("⚠️ 금액은 음수일 수 없습니다.")
                continue
            break
        except ValueError:
            print("⚠️ 금액은 숫자만 입력해주세요.")

    # 딕셔너리 구성 & 리스트에 추가
    item = {
        "날짜": date,
        "분류": category,
        "내용": content,
        "금액": amount
    }

    account_list.append(item)
    print("✅ 항목이 추가되었습니다!")

def print_list():
    if not account_list:
        print("⚠️ 등록된 항목이 없습니다.")
        return

    print("\n📋 가계부 항목 목록")
    print("--------------------------------------------------")
    print("번호 | 날짜        | 분류 | 내용     | 금액")
    print("--------------------------------------------------")
    for idx, item in enumerate(account_list, 1):
        print(f"{idx:>3} | {item['날짜']} | {item['분류']} | {item['내용']} | {item['금액']:,}원")
    print("--------------------------------------------------")


def delete_item():
    if not account_list:
        print("⚠️ 삭제할 항목이 없습니다.")
        return

    try:
        delete_acc = int(input("삭제할 항목 번호를 입력하세요: "))
    except ValueError:
        print("⚠️ 숫자를 입력해주세요.")
        return

    if not (1 <= delete_acc <= len(account_list)):
        print("⚠️ 유효하지 않은 번호입니다.")
        return

    item = account_list[delete_acc - 1]
    confirm = input(f"정말로 '{item['내용']}' 항목을 삭제하시겠습니까? (y/n): ")
    if confirm.lower() == 'y':
        del account_list[delete_acc - 1]
        print(f"✅ '{item['내용']}' 항목이 삭제되었습니다.")
    else:
        print("❎ 삭제가 취소되었습니다.")


def show_summary():
    income_sum = 0
    outcome_sum = 0

    print("💰 총합 계산 결과\n------------------------")
    
    for i in account_list:
        if i['분류'] == '지출':
            outcome_sum += i['금액']
        elif i['분류'] == '수입':
            income_sum += i['금액']
        else:
            print(f"⚠️ 알 수 없는 항목: {i}")

    if income_sum == 0:
        print("수입 내역이 없습니다.")
    else:
        print("총 수입: %d원"%(income_sum))

    if outcome_sum == 0:
        print("지출 내역이 없습니다.")
    else:
        print("총 지출: %d원"%(outcome_sum))
    print("순 자산: %d원\n------------------------"%(income_sum-outcome_sum))

def save_data():
    last = input("정말 저장할까요? (y/n): ")
    if last.lower() == 'y':
        with open("account_book.txt", "w", encoding="utf-8") as f:
            json.dump(account_list, f, ensure_ascii=False, indent=2)
            print("총 %d개의 항목이 저장되었습니다." % len(account_list))

def load_data():
    global account_list
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            account_list = json.load(f)
            print(f"✅ {len(account_list)}개의 항목을 불러왔습니다.")
    except FileNotFoundError:
        print("📂 저장된 파일이 없습니다. 새로 시작합니다.")
        account_list = []
    except json.JSONDecodeError:
        print("⚠️ 파일 형식이 잘못되었습니다. 새로 시작합니다.")
        account_list = []
