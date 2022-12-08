lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
dup = []
for i in lst:
    if lst.count(i) > 1:
        dup.append(i)
print(dup)
print(list(dict.fromkeys(dup)))
