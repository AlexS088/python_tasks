n = int(input())
first = 0
second = 0
for i in range (n):
    n = int(input())
    if n > first:
        second = first
        first = n
    elif second < n < first:
        second = n
print(first)
print(second)