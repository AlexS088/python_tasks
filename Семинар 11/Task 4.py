s = input().split()
for i in range (len(s)):
    s[i] = int(s[i])
def summa(s: list) -> float:
     return sum(s)
def average_ls(s) -> float:
   avg = sum(s) / len(s)
   return avg
print(summa(s))
print(average_ls(s))
