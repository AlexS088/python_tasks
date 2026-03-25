st = input().split(',')
for i in range(len(st)):
    st[i] = int(st[i])
def validation(st: list) -> bool:
    for i in range(len(st)):
        if isinstance(st[i], str):
            return False
        elif isinstance(st[i], float):
            return False
        
if validation(st) != False:
    def solving(st: list) -> int:
        result = 0
        for i in range(len(st) -1):
            if st[i] == st[i+1] - 1:
                result += sum(st)
                return result
            else:
                return "Invalid input"
            
if validation(st) == False:
    print("Invalid input")
else:
    print(solving(st))

