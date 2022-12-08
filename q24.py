s1 = "a3f8h1l9h4y2i7w4l5b2n7m3x8"
d = {}
q = 0
for i in s1:
    if i.isdigit():
        d[i] = q
    else:
        q+=1
    
print(d)
