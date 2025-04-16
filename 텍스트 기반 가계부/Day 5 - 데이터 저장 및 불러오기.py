import json

account = [
    {"날짜": "2025-04-02", "분류": "지출", "내용": "커피", "금액": 3000},
    {"날짜": "2025-04-03", "분류": "수입", "내용": "월급", "금액": 2000000},
    {"날짜": "2025-04-03", "분류": "지출", "내용": "점심", "금액": 8000}
]

#account.txt
last = input("정말 저장할까요? (y/n): ")
if last.lower() == 'y':
    with open("account.txt", "w", encoding="utf-8") as f:
        json.dump(account, f, ensure_ascii=False, indent=2)
        print("총 %d개의 항목이 저장되었습니다." % len(account))

try:
    with open("account.txt", "r", encoding="utf-8") as f:
        account = json.load(f)
except FileNotFoundError:
    account = []