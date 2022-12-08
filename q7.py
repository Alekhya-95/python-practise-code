s = "hello world"

temp = s.split()
d = []
for j in temp:
        q = j[0].upper() + j[1:] +j[-1].upper()
        d.append(q)
print(d)