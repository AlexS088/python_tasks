numbers = input()
splited = numbers.split()
for i in range(len(splited)):
    splited[i] = int(splited[i])
def solve_lst(splited: list) -> list:
    result = []
    for i in range(len(splited)):
        if splited[i] >= 0:
            result.append(splited[i])
    return result
print(solve_lst(splited))
