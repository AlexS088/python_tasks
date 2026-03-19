st = input().split()
sync = 0
for u in range(len(st)):
    for j in range (u+1,len(st)):
        if st[u] == st[j]:
            sync += 1
print(sync)