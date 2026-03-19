n = int(input())
s = []
for i in range (n):
    num = int(input())
    s.append(num)
del s[1::2] 
print(s)