input_string = input()
numbers = []
current_number = ""

for char in input_string:
    if char.isdigit():
        current_number += char
    else:
        if current_number:
            numbers.append(int(current_number))
        current_number = ""

if current_number:
    numbers.append(int(current_number))

total_sum = sum(numbers)
average = round(total_sum / len(numbers), 2)

print(total_sum)
print(average)