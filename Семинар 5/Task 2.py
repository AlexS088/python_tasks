st = input()
flag = True
counter = 0
while flag:
    st = input()
    counter += 1
    if st == "ХВАТИТ" or st == "ДОСТАТОЧНО" or st == "СТОП":
        flag = False
print(counter)