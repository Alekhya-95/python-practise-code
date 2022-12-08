s = "Alekhya"

i = 3
for i in range(len(s)):
    if i == 3:
        temp = s[i]
        f = s[0:i]+s[i+1:]

print(f)