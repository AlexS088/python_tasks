nums = input().split()
def is_positive(nums: int) -> bool:
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    for i in range(len(nums)):
        if nums[i] >= 0:
            return True
        else:
            return False
def count_positive(nums: list) -> int:
    count_pos = 0
    for _ in range(len(nums)):
        if is_positive(nums) == True:
            count_pos += 1
    return count_pos
def count_negative(nums: list) -> int:
    count_neg = 0
    for i in range(len(nums)):
        if nums[i] < 0:
            count_neg += 1 
    return count_neg          
print(f"Количество положительных чисел: {count_positive(nums)}")
print(f"Количество отрицательных чисел: {count_negative(nums)}") #НЕПРАВИЛЬНО
for i in range(len(nums)):
    print(is_positive(nums))
