import re

task = 0
number_mapping = {
    'eight': 8, '8': 8,
    'seven': 7, '7': 7,
    'three': 3, '3': 3,
    'four': 4, '4': 4,
    'five': 5, '5': 5,
    'nine': 9, '9': 9,
    'six': 6, '6': 6,
    'one': 1, '1': 1,
    'two': 2, '2': 2
}
pattern = re.compile('|'.join(number_mapping.keys()))

for line in open('basic.txt'):
    print(line)

    matches = pattern.finditer(line)
    leftmost_match = next(matches, None)
    rightmost_match = None

    for match in matches:
        print(match)
        rightmost_match = match

    if rightmost_match and leftmost_match is not None:
        leftmost_number = number_mapping[leftmost_match.group()]
        print("leftmost number is ", leftmost_number)
        rightmost_number = number_mapping[rightmost_match.group()]
        print("rightmost_number is ", rightmost_number)
        line_sum = str(leftmost_number) + str(rightmost_number)
        print("line_sum is ", line_sum)
        task += int(line_sum)
        print("---")
print(task)
