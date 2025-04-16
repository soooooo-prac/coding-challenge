list_money = {}

list_money['날짜'] = input("날짜를 입력하세요 (예: 2025-04-02): ")
list_money['분류'] = input("분류를 입력하세요 (수입 또는 지출): ")
list_money['내용'] = input("내용을 입력하세요 (예: 점심): ")
list_money['금액'] = int(input("금액을 입력하세요 (숫자): "))

print("[항목이 추가되었습니다!]")
print(list_money)