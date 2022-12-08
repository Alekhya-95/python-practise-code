input_list = [[1, 2], [3,4], [5,6], [7,8]]
# Output:
# [[1, 3, 5, 7], [2, 4, 6, 8]]"
a1 = []
a2 = []
# print(input_list[0])
a = [input_list[i][0] for i in range(len(input_list))]
print(a)
b = [input_list[j][1] for j in range(len(input_list))]
print(b)
final = []
final.append(a)
final.append(b)
print(final)