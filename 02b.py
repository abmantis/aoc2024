# read data.txt file

reports = []


def is_safe_faster(report: list[str], dampen=True) -> bool:
    l1 = int(report[0])
    l2 = int(report[1])
    increasing = l1 < l2
    for i in range(len(report) - 1):
        l1 = int(report[i])
        l2 = int(report[i + 1])
        diff = l1 - l2
        abs_diff = abs(diff)
        if increasing != (diff < 0) or abs_diff < 1 or abs_diff > 3:
            if dampen:
                if i == 1:  # dampen the first being inverted
                    drop_prev = report[: i - 1] + report[i:]
                    if is_safe_faster(drop_prev, False):
                        return True
                drop_l1 = report[:i] + report[i + 1 :]
                if is_safe_faster(drop_l1, False):
                    return True
                drop_l2 = report[: i + 1] + report[i + 2 :]
                if is_safe_faster(drop_l2, False):
                    return True
            return False
    return True


def is_safe(report: list[str]) -> bool:
    l1 = int(report[0])
    l2 = int(report[1])
    increasing = l1 < l2
    for i in range(len(report) - 1):
        l1 = int(report[i])
        l2 = int(report[i + 1])
        diff = l1 - l2
        if increasing != (diff < 0):
            return False
        if abs(diff) < 1:
            return False
        if abs(diff) > 3:
            return False
    return True


def is_safe_dampened(report: list[str]) -> bool:
    if is_safe(report):
        return True

    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1 :]):
            return True
    return False


with open("02data.txt", "r") as input_data:
    for line in input_data.read().splitlines():
        reports.append(line.split(" "))

safe_reports = 0
for report in reports:
    if is_safe_faster(report):
        safe_reports += 1
print(safe_reports)
