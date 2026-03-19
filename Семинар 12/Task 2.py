text = input()
def all_unique(text: str) -> bool:
    for i in range (len(text)):
        if text.count(text[i]) > 1:
            return False
    return True
print(all_unique(text))