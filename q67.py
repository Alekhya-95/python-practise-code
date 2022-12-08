# Find the number of pairs in an array which sum upto 8
import random

a = []
size =5
sum=3

for i in range(size):
    s = random.randint(0,9)
    a.append(s)
print(a)

for p in range(1,len(a)+1):
    for q in a[p+1:]:
    # d = sum - p
        if p + q == sum:
            print("Pair:", p,q)
