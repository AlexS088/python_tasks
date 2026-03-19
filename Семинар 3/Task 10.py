a, b, c = int(input()),int(input()),int(input())
if a == b == c:
    print("Равносторонний")
elif a == b or a == c or b == c:
    print("Равнобедренный")
elif a != b and b != c and a != c:
    print("Разносторонний")
# elif a >= b+c or b >= a + c or c >= b + a: #Нужно персмотреть
#     print("Такой треугольник невозможен")