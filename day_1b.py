ttn = {"zero": 0, "one": 1, "two": 2, "three": 3,
       "four": 4, "five": 5, "six": 6, "seven": 7,
       "eight": 8, "nine": 9,
       "0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,
       "7":7,"8":8,"9":9}

def getFirstLast(puzzle_input):
    total = 0
    digits = "0123456789"
    for i in puzzle_input.split('\n'):
        first = 0
        found = False
        firstDigit = ""
        while ((not found) and (not  first > len(i))):
            for j in range(0, 10):
                try:
                    firstDigit = ttn[i[first:first+j]]
                    found = True
                    break
                except:
                    found = False
            if (not found): first += 1
        lastDigit = ""
        last = len(i) - 1
        found = False
        while ((not found) and (not last < 0)):
            for j in range(0, 10):
                try:
                    lastDigit = ttn[i[last-j:last+1]]
                    found = True
                    break
                except:
                    found = False
            if (not found): last -= 1
        total += int(str(firstDigit) + str(lastDigit))
    return total

print(getFirstLast(open("input.txt", 'r').read()))
