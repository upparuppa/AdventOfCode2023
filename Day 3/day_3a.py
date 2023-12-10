puzzle = [list(i) for i in open("input.txt", 'r').read().split("\n")]
digits = "0123456789"
first_few = 0
total = 0
for i in range(0, len(puzzle)):
    adjacent =  False
    number = ""
    for j in range(0, len(puzzle[0])):
        digit = puzzle[i][j]
        if digit in digits:
            if not adjacent:
                for k in range(-1,2):
                    for m in range(-1,2):
                        if (not (i+k < 0) and not (i+k>=len(puzzle))) and (not (j+m < 0) and not (j+m>=len(puzzle[0]))):
                            point = puzzle[i+k][j+m]
                        else:
                            point = "."
                        if point != "." and point not in digits:
                            adjacent = True
 
                            
        if digit in digits:
            number += digit
        if digit not in digits and number != "":
            if not adjacent:
                print(number)
            if adjacent:
                total += int(number)
            number = ""
            adjacent = False
    if adjacent and number != "":
        total += int(number)
print(total)
