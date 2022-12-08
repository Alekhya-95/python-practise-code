s = "GeeksforGeeks"
d = {}
for i in s:
    d[i] = s.count(i)

print(d)
print(d.values())
a = max(d.values())
# print(a)
# print(d.get(a))
# s = [key for key, val in d.values() if max(val)]
for k, v in d.items():
    if v == a:
        print("max occurance char:", k)