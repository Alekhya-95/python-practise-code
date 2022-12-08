"""
For example, if s = 'azcbulbulbegghakl', then your program should print 2 for word 'bulb'
"""

def wordCount(*args):
    try:
        l = len(subset)
        res = 0
        start = 0
        stop = l
        while stop != len(s)-1:
            a = s[start:stop]
            # print(a)
            if a == subset:
                res +=1
                start+=1
                stop+=1
            else:
                start+=1
                stop+=1
        return res
    except Exception as e:
        print("Unable to get word count: ", e)

s = 'azcbulbulbegghakl'
subset = 'bulb'
print(wordCount(s, subset))
"""
select aadhar_no from table Not in (select distinct aadhar_no from table)
"""

