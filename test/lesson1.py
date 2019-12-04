list_1 = [1, 2, (1, 4), 4, 5]
print(list_1[2])
tuple_1 = (1, 2, 3, 4, 5)
print(tuple_1[1])
t = 1, 2, 3, 4, 5
print(type(t))

dict_1 = {
    2: 'jkhkj',
    'dsfsdf': 5,
    (1,2): 3,
}

print(dict_1[2], dict_1['dsfsdf'])

print(hash('one'))
print(hash('One'))
print(bool((1,2,3,4,5)))

a = 2
b = 2
print(id(a),id(b))
print(id(a) is id(b))

a = 1000000
b = 1000000
print(id(a),id(b))
print(id(a) is id(b))
