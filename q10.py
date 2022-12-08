s = "geeksforgeeks"
sub = 'geeks'
des = 'sony'

start = 0
stop = len(sub)
while stop != len(s) -1:
    a = s[start:stop]
    if a == sub:
        s = s.replace(sub, des)
        start +=1
        stop +=1
    else:
        start +=1
        stop +=1
        

print(s)