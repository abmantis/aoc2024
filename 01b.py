# read data.txt file

sum = 0
right_numbers = []
left_numbers = []

with open("01data.txt", "r") as input_data:
    for line in input_data.read().splitlines():
        numbers = line.split("   ")
        left_numbers.append(int(numbers[0]))
        right_numbers.append(int(numbers[1]))

similarity = 0
for left_nr in left_numbers:
    right_counts = right_numbers.count(left_nr)
    similarity += left_nr * right_counts

print(similarity)
