number_mapping = {
    'one': 1, '1': 1,
    'two': 2, '2': 2,
    'three': 3, '3': 3,
    'four': 4, '4': 4,
    'five': 5, '5': 5,
    'six': 6, '6': 6,
    'seven': 7, '7': 7,
    'eight': 8, '8': 8,
    'nine': 9, '9': 9
}
list_pattern = number_mapping.keys()


def find_forward(line: str, patt: list):  # solves part 1
    leftmost_index = len(line)
    current_item = None

    for item in patt:
        index = line.find(item)
        if index != -1 and (index is None or index < leftmost_index):
            leftmost_index = index
            current_item = item

    return str(number_mapping[str(current_item)])


def find_backward(line: str, patt: list):  # required for part2
    reversed_patt = [item[::-1] for item in patt]
    reversed_line = line[::-1]
    rightmost_index = len(reversed_line)
    current_item = None
    for item in reversed_patt:
        index = reversed_line.find(item)
        if index != -1 and (index is None or index < rightmost_index):
            rightmost_index = index
            current_item = item[::-1]

    return str(number_mapping[str(current_item)])


file = open("input.txt")
task = 0
for string in file:
    leftmost_num = find_forward(string, list_pattern)
    rightmost_num = find_backward(string, list_pattern)
    line_num = leftmost_num + rightmost_num
    task += int(line_num)
    print(string)
    print("Leftmost: " + leftmost_num)
    print("Rightmost: " + rightmost_num)
    print("Concatenated line number: " + line_num)
    print("Current sum: " + str(task))
    print("---")
