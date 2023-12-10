puzzle = [list(i) for i in open("input.txt", 'r').read().split("\n")]
digits = "0123456789"
gear_numbers = []
gear_coordinates = []
first_few = 0
for i in range(0, len(puzzle)):
    is_gear =  False
    number = ""
    for j in range(0, len(puzzle[0])):
        digit = puzzle[i][j]
        if digit in digits:
            if not is_gear:
                for k in range(-1,2):
                    for m in range(-1,2):
                        if (not (i+k < 0) and not (i+k>=len(puzzle))) and (not (j+m < 0) and not (j+m>=len(puzzle[0]))):
                            point = puzzle[i+k][j+m]
                        else:
                            point = "."
                        if point == "*":
                            is_gear = True
                            coordinate = f"{i+k}-{j+m}"
 
                            
        if digit in digits:
            number += digit
        if digit not in digits and number != "":
            if is_gear:
                gear_numbers.append(number)
                gear_coordinates.append(coordinate)
            number = ""
            is_gear = False
    if is_gear and number != "":
        gear_numbers.append(number)
        gear_coordinates.append(coordinate)
repeat_coordinate = []
repeat_times = []
for i in gear_coordinates:
    if i in repeat_coordinate:
        index = repeat_coordinate.index(i)
        repeat_times[index] += 1
    else:
        repeat_coordinate.append(i)
        repeat_times.append(1)
index = 0
total = 0
for i in repeat_times:
    if i == 2:
        values = []
        index_j = 0
        for j in gear_coordinates:
            if j == repeat_coordinate[index]:
                values.append(int(gear_numbers[index_j]))
            index_j += 1
        total += values[0] * values[1]
    index += 1
print(total)
