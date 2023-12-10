import re

with open("input.txt", 'r') as file:
    g = []
    for i in re.split('\n', file.read()):
        g.append(re.split('; ', re.search(': (.*)', i).group(1)))
    tot = 0
    for i in enumerate(g):
        possible = True
        cols = {'red':0,'green':0,'blue':0}
        for j in i[1]:
            for k in j.split(', '):
                step = k.split(' ')
                if int(step[0]) > cols[step[1]]:
                    cols[step[1]] = int(step[0])
            power = 1
        for value in cols.values():
            power = power * value
        tot+=power
    print(tot)
            
