my_str = "wind"
my_int = 5
my_float = 15.5
my_byt = bytes([5,3])
my_list = ["september", 15, 'december', 30.5, 15]
my_tuple = ('sun', 16, 3.5, 15)
my_set = {"cold", 25.5, 31, 'warm'}
my_frzs = frozenset({"cloud", 'rain'})
my_dict = {'name': 'Kostia',
           'age': 6,
           'city': "Vitebsk"}

new_list = [my_str, my_int, my_float, my_byt, my_list, my_tuple, my_set, my_frzs, my_dict]

for i in new_list:
    print('param =', i, '-', type(i))



a = 'See '
b = 'the rainbow!'
c = a + b

print(c)



d = 55
e = -2
f = d + e

print('f =', f, '-', type(f))

g = d / e
print('g =', g, '-', type(g))

h = d * e
print('h =', h, '-', type(h))

j = d // e
print('j =', j, '-', type(j))

k = d % e
print('k =', k, '-', type(k))
d += k
print('d =', d, '-', type(d))
