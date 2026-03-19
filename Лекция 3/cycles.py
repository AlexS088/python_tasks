# counter = 0
# for i in range (5):
#     print("Привет") # Привет 5 раз, и каждый на отдельной строке
# for i in range (10):
#     n = input()
#     if "." in n:
#         counter += 1
# print(counter)
# print("Цикл завершён")
# for i in range (2, 4):
#     print(i)
# for i in range (100, 1000):
#     if i % 10 == 7:
#         print(i)
# for i in range (0, 20, 2): # Откуда начинаем, где заканчиваем, шаг перебора
#     print(i) # Выйдут чётные числа от 0 до 19 включительно (20 не берём!)
# for i in range (10, 0, -1): # Для обратного перебора
#     print(i)
# counter = 0
# right = int(input())
# for i in range (0, right):
#     num = int(input())
#     if num > 10:
#         counter += 1
# print(counter)
# largest = 0
# for _ in range (10):
#     num = int(input()) # Перезаписывание числа и вывод максимального из них
#     if num > largest:
#         largest = num
# print("Наибольшее число равно", largest)
# a = int(input())
# b = int(input())
# counter = 0
# for i in range (a, b+1):
#     if (i**3) % 10 == 4 or (i**3) % 10 == 9:
#         counter += 1
# print(counter)
total = 0
for i in range (1, 6):
    total += i
print(total) # 15