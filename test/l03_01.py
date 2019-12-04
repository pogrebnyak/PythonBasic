a = 'ddddddddddd'
a = list(a)
b = a
print(type(a))
a.append('f')
a = a + ['y', 'f']
print(a, id(a))
print(b, id(b))

a1 = (1,2,3,4,5)
a2 = tuple([5,6,7])
print(a1,type(a1))
print(a2,type(a2))
a3 = tuple(a)
print(a3,type(a3))
print(set(a3),type(a3))
a4 = set([3,2,1])
print(a4)
