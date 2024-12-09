from enum import Enum


class DIRECTIONS(Enum):
    N = 0
    NE = 1
    E = 2
    SE = 3
    S = 4
    SW = 5
    W = 6
    NW = 7

def search_in_direction(input: list[str], to_search: str, line: int, col: int, direction: DIRECTIONS) -> bool:
    if direction == DIRECTIONS.N or direction == DIRECTIONS.NE or direction == DIRECTIONS.NW:
        new_line = line - 1
    elif direction == DIRECTIONS.S or direction == DIRECTIONS.SE or direction == DIRECTIONS.SW:
        new_line = line + 1
    else:
        new_line = line

    if direction == DIRECTIONS.E or direction == DIRECTIONS.NE or direction == DIRECTIONS.SE:
        new_col = col + 1
    elif direction == DIRECTIONS.W or direction == DIRECTIONS.NW or direction == DIRECTIONS.SW:
        new_col = col - 1
    else:
        new_col = col

    if new_line < 0 or new_line >= len(input):
        return False
    if new_col < 0 or new_col >= len(input[new_line]):
        return False

    if input[new_line][new_col] == to_search[0]:
        if len(to_search) == 1:
            return True
        return search_in_direction(input, to_search[1:], new_line, new_col, direction)
    return False

def find_xmas(input: list[str], line: int, col: int) -> int:
    xmas_count = 0
    for direction in DIRECTIONS:
        if search_in_direction(input, "MAS", line, col, direction):
            xmas_count = xmas_count + 1
    return xmas_count




input: list[str] = []
with open("04data.txt", "r") as input_data:
    for line in input_data.read().splitlines():
        input.append(line)

xmas_count = 0
for i in range(len(input)):
    line = input[i]
    x_search_idx = -1
    while True:
        x_search_idx = line.find("X", x_search_idx + 1)
        if x_search_idx < 0:
            break
        xmas_count = xmas_count + find_xmas(input, i, x_search_idx)

print(xmas_count)
