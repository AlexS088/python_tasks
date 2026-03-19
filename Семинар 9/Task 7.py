n = int(input())
s1 = []
s2 = []
s3 = []
result = []
for i in range (n):
    num = int(input())
    if num < 0:
        s1.append(num)
    elif num == 0:
        s2.append(num)
    elif num > 0:
        s3.append(num)
result.extend(s1)
result.extend(s2)
result.extend(s3)
print(result)
