def hackers_security(hackers: list, security_level: int, increase: int) -> int:
    count_burgle = 0
    if hackers == "":
        return 0
    elif hackers != "":
        for i in range(len(hackers)):
            if hackers[i] <= security_level:
                security_level += increase
            elif hackers[i] > security_level:
                count_burgle += 1
    return count_burgle
print(hackers_security([1,2,5,7,9,2,34,5],5,1))
