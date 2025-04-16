import json
from datetime import datetime

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

account = {"날짜": date, "분류": category, "내용": content, "금액": amount}

try:
    with open("Day6.txt", "w", encoding="utf-8") as f:
        json.dump(account, f, ensure_ascii=False, indent=2)
except json.JSONDecodeError:
    print("⚠️ 저장된 파일을 읽을 수 없습니다. 새로운 데이터로 시작합니다.")
    account = []
    
print("📋 가계부 항목 목록\n--------------------------------------------------\n날짜        | 분류 | 내용     | 금액")
print(f"날짜: {account['날짜']} | 분류: {account['분류']} | 내용: {account['내용']} | 금액: {account['금액']:,}원")
print("--------------------------------------------------")