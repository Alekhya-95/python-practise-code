a =  [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
# The mapped Dictionary : {(‘c’, ‘d’): (3, 4), (‘e’, ‘f’): (5, 6), (‘a’, ‘b’): (1, 2)}
m={}
d = {}
for i in a:
    t1 = (i[0], i[1])
    t2 = (i[2], i[3])
    d[t1]=t2
    m.update(d)

print(m)


