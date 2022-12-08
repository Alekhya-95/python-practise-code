list1 = [2, 7, 5, 64, 14]

s = len(list(filter(lambda i :(i%2==0),list1)))
#print(s)

#or
i = 0
even =0
odd = 0
while i< len(list1):
    if list1[i] %2 ==0:
        even+=1
    else:
        odd+=1
    i+=1

print(even)