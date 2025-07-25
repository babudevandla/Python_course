set1 = {'Avengers','IranMan','Hitman'}
set2 = {'Avengers','IranMan','Hitman','Hulk'}
print('Set1: ', set1)
print('Set2: ',set2)
print('--------------')
set1.add('SuperMan ')
print('Set1: ', set1)
print(set2.difference(set1))
print(set2)
print('-----------')
print(set1.intersection(set2))
print('--------------')
set2.difference_update(set1)
print(set2)
set2.intersection_update(set1)
print(set2.union(set1))


