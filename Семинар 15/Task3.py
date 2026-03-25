st = input().split(',')
def validation(st: list) -> bool:
    all_nums = "0123456789"
    if len(st) != 3:
        return False
    for i in range(len(st)):
        if st[i] not in all_nums:
            return False
        
if validation(st) != False:
    def solving(st: list) -> int:
        for i in range(len(st)):
            st[i] = int(st[i])
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

