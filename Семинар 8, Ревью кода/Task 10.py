n = int(input())
d = 0
for i in range (1, n):
    i = int(input())
    if n % i == 0:
        d = i
print(d) # неправильно