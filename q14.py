from cgi import test


test_dict = {1 : 'Gfg is love', 2: 'Gfg is good', 3:'sony'} 
sub_list = ['love', 'good'] 

res = {key : val for key, val in test_dict.items() if not any(ele in val for ele in sub_list)}
print(res)
d = {}
vals = list(test_dict.values())
print(vals)
for k,v in test_dict.items():
    for i in sub_list:
        if i not in v:
            d.update({k:v})
        

print(d)