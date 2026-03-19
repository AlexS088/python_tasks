st = input()
ln = len(st)
counter_plus = 0
counter_multiply = 0
for i in st:
    if i == "*":
        counter_multiply += 1
    elif i == "+":
        counter_plus += 1
print(counter_multiply)
print(counter_plus)
