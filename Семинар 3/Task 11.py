num1 = int(input())
num2 = int(input())
operation = input()
if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/" and num2 == 0:
    print("На ноль делить нельзя!")
elif operation == "//" and num2 == 0:
    print("На ноль делить нельзя!")          #ВАЖЕН ПОРЯДОК УСЛОВИЙ, ИНАЧЕ БУДЕТ НЕПРАИЛЬНО РАБОТАТЬ!
elif operation == "%" and num2 == 0:
    print("На ноль делить нельзя!")
elif operation == "/":
    print(num1/num2)
elif operation == "//":
    print(num1//num2)
elif operation == "%":
    print(num1 % num2)
elif operation == "**":
    print(num1**num2)


