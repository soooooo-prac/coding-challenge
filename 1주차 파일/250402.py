# Day 2
try:
    num = int(input("숫자를 입력하세요: "))
    if num < 0 or num >= 1000:
        print("범위를 벗어난 숫자입니다.")
    elif num % 2 == 0:
        print("짝수입니다.")
    else:
        print("홀수입니다.")
except ValueError:
    print("숫자를 입력해주세요.")

#Day 3
try:
    num = int(input("출력할 단을 입력하세요 (2~9):"))
    if not 2 <= num <= 9:
        print("2부터 9 사이의 숫자만 입력해주세요.")
    else:
        for i in range(1,10):
            print("%d * %d = %d"%(num,i,num*i))
except ValueError:
    print("2부터 9 사이의 숫자만 입력해주세요.")

#Day 4
try:
    num = list(map(int, input("숫자들을 쉼표로 구분해서 입력하세요: ").split(',')))
    even = 0 #개수
    number = 0 #총합

    for i in num:
        if i%2 == 0:
            even += 1
            number += i
    
    print("짝수 개수: %d"%even)
    print("짝수 합계: %d"%number)
except ValueError:
    print("숫자만 입력해주세요.")