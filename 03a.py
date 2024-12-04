# read data.txt file


def parse_number(input: str) -> int:
    result = ""
    for c in input:
        if c.isdigit():
            result += c  # TODO: use indexes and slice at the end for perf
        else:
            break
    return result


input = ""
with open("03data.txt", "r") as input_data:
    for line in input_data.read().splitlines():
        input += line


sum = 0
search_str = "mul("
mul_idx = input.find(search_str)
while mul_idx > -1:
    next_idx = mul_idx + len(search_str)
    input = input[next_idx:]
    mul_idx = input.find("mul(")

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

    sum += int(n1)*int(n2)
print(sum)
