rules_after: dict[int, list[int]] = {}
rules_before: dict[int, list[int]] = {}
updates: list[list[int]] = []

with open("05data.txt", "r") as input_data:
    parsing_rules = True
    for line in input_data.read().splitlines():
        line = line.strip()
        if len(line) == 0:
            parsing_rules = False
            continue
        if parsing_rules:
            rule = line.split("|")
            n0 = int(rule[0])
            n1 = int(rule[1])

            if n0 not in rules_after:
                rules_after[n0] = []
            rules_after[n0].append(n1)
            if n1 not in rules_before:
                rules_before[n1] = []
            rules_before[n1].append(n0)
        else:
            updates.append([int(v) for v in line.split(",")])


def check_number_rules(update: list[int], idx: int) -> bool:
    nr = update[idx]
    nrs_after = rules_after[nr] if nr in rules_after else []
    nrs_before = rules_before[nr] if nr in rules_before else []

    if set(nrs_after) & set(update[:idx]):
        return False
    if set(nrs_before) & set(update[idx + 1 :]):
        return False
    return True


def is_valid_update(update: list[int]) -> bool:
    for i in range(len(update)):
        if not check_number_rules(update, i):
            return False
    return True


def order_update(update: list[int]):
    for i in range(len(update)):
        nr = update[i]
        nrs_after = rules_after[nr] if nr in rules_after else []
        for j in range(i):
            if update[j] in nrs_after:
                update.insert(j, update.pop(i))
                i = -1
                break


def get_mid_value(update: list[int]) -> int:
    return update[len(update) // 2]


sum = 0
for update in updates:
    if is_valid_update(update):
        continue
    order_update(update)
    sum += get_mid_value(update)
print(sum)
