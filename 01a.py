# read data.txt file

sum = 0
right_numbers = []
left_numbers = []

with open("01data.txt", "r") as input_data:
    for line in input_data.read().splitlines():
        numbers = line.split("   ")
        left_numbers.append(int(numbers[0]))
        right_numbers.append(int(numbers[1]))

left_numbers.sort()
right_numbers.sort()

while len(right_numbers) > 0:
    left = left_numbers.pop()
    right = right_numbers.pop()
    diff = right - left if right > left else left - right
    sum += diff

print(sum)
