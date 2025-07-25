
my_dict = {'Car1': 'Audi', 'Car2': 'Maruthi'}
print(my_dict)
print(len(my_dict))
print(my_dict.get('Car1'))
print(my_dict.get('Car2'))
print('-----------------')
for x in my_dict.items():
    print(x)

print('------------------')
for x in my_dict.keys():
    print(x)

print('------------------')
for x in my_dict.values():
    print(x)

print('------------------')
my_dict['Car3'] = 'BMW'
print(my_dict)
print('------------------')
my_dict.popitem()
print(my_dict)
my_dict.pop('Car2')
print(my_dict)
my_dict['Car1'] = 'Ambassador'
print(my_dict)
