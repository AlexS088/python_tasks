st = input().split('.')
counter = 0
for i in range (len(st)):
    if 0 <= int(st[i]) <= 255:
        counter += 1
if counter == 4:
    print("ДА")
else:
    print("НЕТ")
