s1 = "a3f8h1l9h4y2i7w4l5b2n7m3x8"

# Need to get only numbers
# sort the numbers in desc
# sum the numbers



a = [i for i in s1 if i.isdigit()]
print(a)

a.sort(reverse=True, key=int)
print("sorted: ", a)
# s = lambda i :int(i)
# print(s(a))
q = []
for i in a:
    q.append(int(i))


print(sum(q))