account = [
    {"날짜": "2025-04-02", "분류": "지출", "내용": "커피", "금액": 3000},
    {"날짜": "2025-04-03", "분류": "수입", "내용": "월급", "금액": 2000000},
    {"날짜": "2025-04-03", "분류": "지출", "내용": "점심", "금액": 8000}
]

def calculate_total(account):
    income_sum = 0
    outcome_sum = 0

    print("💰 총합 계산 결과\n------------------------")
    for i in account:
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

calculate_total(account)