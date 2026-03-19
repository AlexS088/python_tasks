def print_case_counts(s: str):
    count_upper = 0
    count_lower = 0
    for i in s:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
    print("Букв в верхнем регистре:", count_upper)
    print("Букв в нижнем регистре:", count_lower)
print_case_counts(input())
