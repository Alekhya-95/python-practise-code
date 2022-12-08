st = "abaxybbyxpq"
n=3

start = 0#++
stop = len(st) #-- 11
res = 0
pal = []
for i in range(stop):
    for j in range(start):
        temp = st[start:stop]
        if temp == temp[::-1]:
            pal.append(temp)
            start = start+1
        else:
            start = start +1
    stop = stop -1

print(pal)
s = [len(p) for p in pal]








while len(st) <= stop:
    temp = st[start:stop]
    if temp == temp[::-1]:
        pal.append(temp)
        start = start+1

