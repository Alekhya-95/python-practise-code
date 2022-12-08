a = [3, 7, 2, 9, 1, 5, 3, 2, 8, 4]
#[3,7,2,9,1,5,8,4]
def functn(a):
    res = list(dict.fromkeys(a))
    return res

# def outer(funct):
#     def inner(a):
#         res = list(dict.fromkeys(a))
#         return funct
#     return res

