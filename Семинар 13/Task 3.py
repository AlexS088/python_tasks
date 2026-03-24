def digits(numbers: str) -> int:
    result_1 = 0
    result_root = 0
    if len(numbers) != 7:
        return "Invalid input"
    splited_nums = numbers.split(',')
    for u in range(len(splited_nums)):
        splited_nums[u] = int(splited_nums[u])
    if [i for i in range(len(splited_nums) - 1) if splited_nums[i] + 1 == splited_nums[i+1]]:
        result_1 = splited_nums[0] * splited_nums[1] * splited_nums[2] * splited_nums[3] + 1
        if result_1 ** 0.5 % 1 == 0:
            result_root = result_1 ** 0.5
            return result_1, result_root
        else:
            return "Root is irracional"
print(digits('1,2,3,4'))
