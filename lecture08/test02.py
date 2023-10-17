# List มีลำดับ
my_list = [10, 20, 10, 'Hi', True, [20, 'Hello'], (10, 20), {10, 20},]
# Tuple มีลำดับ
my_tuple = (10, 20, 10, 'Hi', True, (20, 'Hello'), [10, 20], ('SAU', 'DTI'),)
# print(my_tuple[7][1])
# Set ไม่มีลำดับ
my_set = {10, 20, 10, 'Hi', True, (10, 20)}
# Dicrionary
my_dict = {'name': 'สมชาย',
           'age': 29,
           555: 999,
           'flag': True}

print(my_dict['name'])
my_dict['name'] = 'สมหญิง'
my_dict['magor'] = 'dti'
print(my_dict)
my_dict.pop('name')
my_dict.pop(555)
print(my_dict)
my_dict.popitem()
print(my_dict)

for data in my_dict:
    print(data, end=(' '))
print()
for data in my_dict.keys():
    print(data, end=' ')
print()
for data in my_dict.values():
    print(data, end=' ')

mydict1 = {'a': 10, 'b': 20, 'c': 30}
mydict2 = mydict1
mydict3 = mydict1.copy()
print()
print(mydict2)
print(mydict3)
mydict2['a'] = 999
mydict3['a'] = 888
print('++++++++++++++++++++++++')
print(mydict1)
print(mydict2)
print(mydict3)
