password = input()
def is_password_good(password: str) -> bool:
    counter = 0
    counter_upper = 0
    counter_lower = 0
    counter_digit = 0
    if len(password) >= 8:
        counter = 1
    for i in password:
        if  i.istitle() == True:
            counter_upper += 1
        if i.islower() == True:            # НЕ ЗАБЫВАТЬ СКОБКИ У МЕТОДОВ СТРОК, ИНАЧЕ НЕ БУДУТ РАБОТАТЬ!
            counter_lower += 1
        elif i.isdigit() == True:
            counter_digit += 1
    if counter_upper >= 1 and counter_digit >= 1 and counter_lower >= 1 :
        counter += 3    
    if counter == 4:
        return "ДА"
    
    return "НЕТ"
print(is_password_good(password))