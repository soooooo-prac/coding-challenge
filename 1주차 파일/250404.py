# Day 7
menu = {
    "아메리카노": 2000,
    "카페라떼": 2500,
    "카푸치노": 3000,
    "바닐라라떼": 3000
}

wants = list(str(input("주문할 메뉴를 쉼표로 입력하세요: ").replace(" ","")).split(','))
price = 0

print("🧾 영수증\n ---------------------")

for i in menu:
    if wants.count(i) != 0:
        price += menu[i] * wants.count(i)
        print("%s x %d = %d원"%(i,wants.count(i),wants.count(i)*menu[i]))
print("총 금액: %d원\n ---------------------"%(price))

for i in wants:
    if i not in menu:
        print("[%s]는(은) 메뉴에 없습니다."%i)