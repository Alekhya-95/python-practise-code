s = [2,4,5,7,8,5]

l = len(s)
avg = int(l/2) #3
temp = s[avg]
s[avg] = s[avg-1]
s[avg-1] = temp

print(s)


