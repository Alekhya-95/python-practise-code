num = int(input("Enter a number:"))

factorial = 1
def getFact(num, factorial):
    if num <= 0:
        print("Invalid")
    else:
        for i in range(1, num +1):
            factorial = factorial *i
            # print(factorial)
    # return factorial
    yield factorial

print(getFact(num, factorial))
