# List มีลำดับ
my_list = [10, 20, 10, 'Hi', True, [20, 'Hello']]
print(my_list)
print(len(my_list))
# Tuple มีลำดับ
my_tuple = (10, 20, 10, 'Hi', True, (20, 'Hello'))
print(my_tuple)
print(len(my_tuple))

# Set ไม่มีลำดับ
my_set = {10, 20, 10, 'Hi', True}
print(my_set)
print(len(my_set))

for data in my_set:
    print(data, end='/ ')
print('---------------------')
list_fr_set = list(my_set)
print(list_fr_set)
list_fr_set[0] = 'DTI'
my_set = set(list_fr_set)
print(my_set)
my_set.clear()
print(len(my_set))

my_set1 = {10, 20, 30, 'Hi'}
my_set2 = {10, 'Hello' 'Hi', True}

my_set1.add(999)
my_set1.remove('Hi')
print(my_set1)

print(my_set1.intersection(my_set2))
print(my_set1.union(my_set2))

# print(min(my_set2))
