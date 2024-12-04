# read data.txt file

reports = []


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


with open("02data.txt", "r") as input_data:
    for line in input_data.read().splitlines():
        reports.append(line.split(" "))

safe_reports = 0
for report in reports:
    if is_safe(report):
        print("safe", report)
        safe_reports += 1
    else:
        print("not safe", report)
print(safe_reports)
