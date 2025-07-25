car1_dict = {'Audi':1960,'BMW':1965}
car2_dict = {'Maruthi':1980,'Benz':1950}
car3_dict = {'Skoda':1970,'Ambassador':1985}

car_type = {"Car1": car1_dict, "Car2": car2_dict, "Car3": car3_dict}
print(car_type)
print('-------------------')
print(car_type['Car1'])
print(car_type['Car2'])

print('-----------------')
print(car_type['Car2']['Maruthi'])

print('-------------------')

for x in car_type.keys():
    print(x)

print('-------------------')
for x in car_type.values():
    print(x)
    