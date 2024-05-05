from collections import defaultdict

 #1373 @ 130,274: 15x26
C = defaultdict(int)
for line in open('input/3'):
    words = line.split()
    x,y = words[2].split(',')
    x,y = int(x), int(y[:-1])
    w,h = words[3].split('x')
    w,h = int(w), int(h)
    for dx in range(w):
        for dy in range(h):
            C[(x+dx, y+dy)] += 1

ans = 0
for (r,c),v in C.items():
    if v >= 2:
        ans += 1
print(ans)

