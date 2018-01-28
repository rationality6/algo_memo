import json
dd = []
with open('memo/json_py/movies.json', 'r') as json_data:
    dd = json.load(json_data)
print(dd)
for i in range(len(dd)):
    print(dd[i]['name'])

# print dd["office"]["parking"]["style"]
