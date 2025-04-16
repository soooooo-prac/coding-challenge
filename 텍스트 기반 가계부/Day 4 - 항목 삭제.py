account = [
    {"날짜": "2025-04-02", "분류": "지출", "내용": "커피", "금액": 3000},
    {"날짜": "2025-04-03", "분류": "수입", "내용": "월급", "금액": 2000000},
    {"날짜": "2025-04-03", "분류": "지출", "내용": "점심", "금액": 8000}
]

for idx, i in enumerate(account, 1):
    print(f"[{idx}] 날짜: {i['날짜']} | 분류: {i['분류']} | 내용: {i['내용']} | 금액: {i['금액']}원")

delete_acc = int(input("삭제할 항목 번호를 입력하세요: "))
# delete_acc2 = input("삭제할 항목의 내용을 입력하세요: ")
real_del = input("정말 삭제하시겠습니까? (y/n): ")

if real_del.lower() == 'y':
    for idx, i in enumerate(account, 1): #시작 인덱스를 1부터
        if idx == delete_acc:
            print(f"→ '{i['내용']}' 항목이 삭제되었습니다!")
            del account[idx - 1]
            break  # 삭제했으면 반복 종료

    # for i in account:
    #     if account.index(i)+1 == delete_acc:
    #         print(f"→ '{i['내용']}' 항목이 삭제되었습니다!")
    #         del account[delete_acc-1]

    # for i in account:
    #     if i["내용"] == delete_acc2:
    #         print(f"→ '{i['내용']}' 항목이 삭제되었습니다!")
    #         del account[account.index(i)]