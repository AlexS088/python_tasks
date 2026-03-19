digit_4sim = int(input())
num1 = digit_4sim // 1000
num2 = (digit_4sim // 100) % 10
num3 = (digit_4sim // 10) % 10
num4 = digit_4sim % 10
if num1 + num4 == num2 - num3:
    print("ДА")
else:
    print("НЕТ")