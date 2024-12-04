# read data.txt file


MUL_STR = "mul("


def parse_number(input: str) -> int:
    result = ""
    for c in input:
        if c.isdigit():
            result += c  # TODO: use indexes and slice at the end for perf
        else:
            break
    return result


def is_mul(input: str) -> bool:
    return input.startswith(MUL_STR)


def is_do(input: str) -> bool:
    return input.startswith("do()")


def is_dont(input: str) -> bool:
    return input.startswith("don't()")


def find_mul(input: str) -> int:
    skip_mul = False
    for i in range(len(input)):
        test = input[i:]
        if is_dont(test):
            skip_mul = True
            continue
        if is_do(test):
            skip_mul = False
            continue
        if not skip_mul and is_mul(test):
            return i + len(MUL_STR)
    return -1


input = ""
with open("03data.txt", "r") as input_data:
    for line in input_data.read().splitlines():
        input += line


print(input)
sum = 0
next_idx = find_mul(input)
while next_idx > -1:
    input = input[next_idx:]
    next_idx = find_mul(input)

    n1 = parse_number(input)
    n1_len = len(n1)
    if n1_len == 0:
        continue
    if input[n1_len] != ",":
        continue

    n2 = parse_number(input[n1_len + 1 :])
    if len(n2) == 0:
        continue
    if input[n1_len + 1 + len(n2)] != ")":
        continue
    print(input)
    print(n1 + "*" + n2)
    sum += int(n1) * int(n2)
print(sum)
