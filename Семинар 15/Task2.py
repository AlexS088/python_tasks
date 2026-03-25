st = input().strip()
def solve_string(st: str) -> str:
    result = ""
    if len(st) % 2 == 0:
        result += st.upper()
    if len(st) % 2 == 1:
        result += st.lower()
    return result
print(solve_string(st))