def solution():
    pass


phone_book = {"sam": 9991222}

for i in range
try:
    print(phone_book['sam'])
except:
    print('nope')


list0 = []

count = int(input())
for i in range(count):
    list0.append([input().split(' ')])


list0 = [['sam', 99912222], ['tom', 11122222], ['harry', 12299933]]
dict0 = {}
for k, v in list0:
    dict0[k] = v

print(dict0)


list0 = []
count = int(input())
for i in range(count):
    list0.append(input().split(' '))

dict0 = {}
for k, v in list0:
    dict0[k] = v

for i in range(count):
    key = input()
    try:
        print("{}={}".format(key,dict0[key]))
    except:
        print('Not found')
