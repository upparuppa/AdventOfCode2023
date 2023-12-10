
import re

tot = 0
with open("input.txt", 'r') as file:
    for i in re.split(r'\n+', file.read()):
        a = [[int(i) for i in re.split(r'\s', i)]]
        last = 0
        while (len(set(a[-1])) != 1 or a[-1][0] != 0):
            curr = a[last]
            diff = [curr[i+1] - curr[i] for i in range(len(curr)-1)]
            a.append(diff)
            last += 1
            
        a[-1].append(0)
        for i in range(len(a)-2, -1, -1):
            a[i].append(a[i][-1]+a[i+1][-1])
        pred_val = a[0][-1]
        tot += pred_val
    print(tot)
        
