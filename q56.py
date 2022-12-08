l = [2,3,6,2,7]
res = []
for i in range(len(l)):
    # print(l[i+1:])
    if l[i] in l[i+1:]:
        continue
    else:
        res.append(l[i])

print(res)