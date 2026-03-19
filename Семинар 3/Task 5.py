age = int(input())
if 0 < age <= 13:
    print("Детство")
elif 14 <= age <= 24:
    print("Молодость")
elif 25 <= age <= 59:
    print("Зрелость")        #Важно проверять границы!
elif age >= 60:
    print("Старость")
else:
    print("Неизвестный возраст")