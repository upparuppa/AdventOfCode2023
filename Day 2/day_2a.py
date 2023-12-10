import re

with open("input.txt", 'r') as file:
    accepted={'red':12,'green':13,'blue':14}
    g_id = []
    g = []
    for i in re.split('\n', file.read()):
        g_id.append(int(re.search('Game (.*):', i).group(1)))
        g.append(re.split('; ', re.search(': (.*)', i).group(1)))
    tot = 0
    for i in enumerate(g):
        possible = True
        for j in i[1]:
            cols = {'red':0,'green':0,'blue':0}
            for k in j.split(', '):
                step = k.split(' ')
                cols[step[1]] += int(step[0])
            for key in cols:
                if cols[key] > accepted[key]:
                    possible = False
        if possible:
            tot += g_id[i[0]]
    print(tot)
            
