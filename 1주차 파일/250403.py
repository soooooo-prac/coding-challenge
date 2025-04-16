# Day 5
m = str(input("문장을 입력하세요: "))
mun = m.split(' ')
mo = ['a', 'e', 'i', 'o', 'u']
result = 0

for i in mun:
    for j in i:
        if j.lower() in mo:
            result += 1

print("모음 개수: %d"%result)

#보너스
for i in mo:
    print('%s: %d'%(i,m.count(i)))

# Day 6
menu = {
    "아메리카노": 2000,
    "카페라떼": 2500,
    "카푸치노": 3000,
    "바닐라라떼": 3000
}

want = str(input("주문할 메뉴를 입력하세요: "))

if want in menu:
    print("%s의 가격은 %d원입니다."%(want,menu[want]))
else:
    print("해당 메뉴는 없습니다.")

#보너스
wants = list(str(input("주문할 메뉴를 쉼표로 입력하세요: ")).split(','))
price = 0

for i in wants:
    if i in menu:
        price += menu[i]
    else:
        print("%s는(은) 메뉴에 없습니다."%i)

print("총 금액은 %d원입니다."%(price))