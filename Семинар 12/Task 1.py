target = input()
symbol = input()
def find_all(target: str, symbol: str) -> list:
    s = []
    for i in range(len(target)):
        if target[i] == symbol:
            s.append(i)
    return s
print(find_all(target, symbol))
    
