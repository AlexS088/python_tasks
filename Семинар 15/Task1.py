num = input()
numbers = num.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
def is_zero(num: int) -> bool:
    if num == 0:
        return True
    else:
        return False
        
def count_zeros(numbers: list) -> int:
    counter_zeros = 0
    for i in range(len(numbers)):
        if is_zero(numbers[i]) == True:
            counter_zeros += 1
    return counter_zeros

def count_nonzeros(numbers: list) -> int:
     counter_nonzeros = 0
     for i in range(len(numbers)):
        if is_zero(numbers[i]) == False:
            counter_nonzeros += 1
     return counter_nonzeros
print(count_zeros(numbers))
print(count_nonzeros(numbers))

         

