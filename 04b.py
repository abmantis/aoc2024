from enum import Enum


def find_xmas(input: list[str], line: int, col: int) -> int:
    nw = input[line - 1][col - 1]
    ne = input[line - 1][col + 1]
    sw = input[line + 1][col - 1]
    se = input[line + 1][col + 1]

    if nw == "M":
        if se != "S":
            return False
    elif nw == "S":
        if se != "M":
            return False
    else:
        return False

    if ne == "M":
        if sw != "S":
            return False
    elif ne == "S":
        if sw != "M":
            return False
    else:
        return False
    return True


input: list[str] = []
with open("04data.txt", "r") as input_data:
    for line in input_data.read().splitlines():
        input.append(line)

xmas_count = 0
for i in range(1, len(input) - 1):
    line = input[i]
    a_search_idx = -1
    while True:
        a_search_idx = line.find("A", a_search_idx + 1)
        if a_search_idx < 0:
            break
        if a_search_idx < 1 or a_search_idx >= len(line) - 1:
            continue

        if find_xmas(input, i, a_search_idx):
            xmas_count = xmas_count + 1
print(xmas_count)
