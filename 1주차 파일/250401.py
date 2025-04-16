# Day 1
num1 = int(input('첫 번째 숫자를 입력하세요: '))
num2 = int(input('두 번째 숫자를 입력하세요: '))

print("더하기 결과: %d"%(num1+num2))
print("빼기 결과: %d"%(num1-num2))
print("곱하기 결과: %d"%(num1*num2))
try:
    print("나누기 결과: {:.1f}".format(num1 / num2))
except ZeroDivisionError:
    print("나누기 결과: 0으로는 나눌 수 없습니다.")