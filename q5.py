from cgi import test


test_list = ["Gfg", 3, "is", 8]
key_list = ["name", "id"]

d = []
for i in key_list:
    for j in test_list:
        d.append({i:j})
        break

print(d)