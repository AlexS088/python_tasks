text = input().split()
n = int(input())
def count_word_by_length(text, n) -> int:
    quantity = 0
    for i in text:
        if len(i) == n:
            quantity += 1
    return quantity
print(count_word_by_length(text, n))