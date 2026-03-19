word1, word2 = input(), input()
def is_one_away(word1: str, word2: str) -> bool:
    count = 0
    count_difference = 0
    if len(word1) == len(word2):
        count += 1
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count_difference += 1
    if count_difference == 1:
        count += 1
    if count == 2:
        return True
    else:
        return False
print(is_one_away(word1, word2)) # посмотреть