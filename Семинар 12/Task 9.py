nums = input().split()
size = int(input())
def split_into_chunks(nums: list, size: int) -> list:
    result = []
    for i in nums:
        result.append(nums), sep = size
print(split_into_chunks(nums, size))