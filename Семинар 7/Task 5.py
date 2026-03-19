st = input()
counter = 0
for i in st:
    if i in "0123456789":
        counter += 1
print(counter)