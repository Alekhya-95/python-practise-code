test_list = [{'Gfg': 123, 'best': 10}, {'Gfg': 51, 'best': 7}]
# Output : [[‘Gfg’, ‘best’], [123, 10], [51, 7]]

l = []
for i in test_list:
    l1 = list(i.keys())
    print(l1)
    l2 = list(i.values())
    l.append(l2)

l.append(l1)
print(l)

