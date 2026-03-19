largest_1 = 0
largest_2 = 0
n = int(input())
for i in range (n):
    nn = int(input())
    if nn > largest_1:
        largest_2 = largest_1
        largest_1 = nn
    elif nn > largest_2:
        largest_2 = nn
print(largest_1, largest_2)
