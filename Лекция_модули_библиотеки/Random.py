import random # Случайные события и так далее
num1 = random.randint(0, 17) # Случайное число из промежутка
num2 = random.randint(-5, 5) # То же самое
print(num1), print(num2)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers) # Случайным образом перемешивает эелементы спска
print(numbers)
print(random.choice("ABCDEFG")) # Случайная буква отсюда
print(random.choice("123456789")) # Случайная цифра отсюда