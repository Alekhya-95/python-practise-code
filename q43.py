"""
obj = B(4)
print(obj.num)
 
obj.mul_two()
print(obj.num)
 
obj.mul_three()
print(obj.num)
"""

class A:

    def __init__(self, a):
        self.a = a

    def mul_two(self):
        return self.a *2


class B(A):

    def __init__(self, a):
        super().__init__(a)

    def mul_three(self):
        return self.a *3

obj = B(4)
print(obj.mul_two())
print(obj.mul_three())