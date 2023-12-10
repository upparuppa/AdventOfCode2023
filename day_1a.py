import string

def getFirstLast(puzzle_input):
    total = 0;
    for i in puzzle_input.split('\n'):
        first = 0
        last = len(i) - 1
        while (not i[first].isnumeric()) or (not i[last].isnumeric()):
            if (not i[first].isnumeric()): first += 1
            if (not i[last].isnumeric()): last -= 1
        total += int(i[first] + i[last])
    return total

print(getFirstLast(open("input.txt", 'r').read()))
