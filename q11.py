list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

from operator import itemgetter

print(sorted(list, key=lambda i: i['age']))