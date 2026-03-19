innocents = [1, 5, 9, 10, 33, 70]
suspects = [2, 5, 7, 10, 23, 105]
clean_list = []
for i in innocents:
    if i not in suspects:
        clean_list.append(i)
print(clean_list)
    