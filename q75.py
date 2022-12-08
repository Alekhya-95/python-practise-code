# x = [1, 4, 2, 5, 6, 8, 3, 1, 8, 9, 13]

# s = [i for i in x if i %2 !=0]
# print(s)
# a = list(dict.fromkeys(s))
# a = set(s)
# print(a)
x = [1, 2, 3, 4, 3, 2, 1, 8, 3, 5, 5, 8, 0, 1, 0]
s = []

for i in x:
    if x.count(i) ==1:
        s.append(i)

print(s)
