st_1 = "Spring!"
st_2 = '25_T_warm'

in_1 = 5
in_2 = 0
in_3 = -10
in_4 = 30

fl_1 = 5.25
fl_2 = -0.75
fl_3 = 10.5

n_l = [st_1,st_2,in_1,in_2,in_3,in_4,fl_1,fl_2,fl_3]
for i in n_l:
    print('Param =', i, ' --', type(i))


a = [in_2,in_3,in_4]
for i in a:
    print('Result =', in_1 > i)

for i in a:
    print('Result =', in_1 < i)

for i in a:
    print('Result =', in_1 >= i)

for i in a:
    print('Result =', in_1 <= i)

for i in a:
    print('Result =', in_1 != i)


b = [fl_2,fl_3]
for i in b:
    print('Result =', fl_1 > i)

for i in b:
    print('Result =', fl_1 < i)

for i in b:
    print('Result =', fl_1 >= i)

for i in b:
    print('Result =', fl_1 <= i)

for i in b:
    print('Result =', fl_1 != i)



result_1 = in_1 == 5 and in_2 >= 0
result_2 = in_1 >= 5 and in_3 != -10
result_3 = in_4 > 15 and in_3 <= -10
result_4 = in_1 > 15 or in_3 <= -15
result_5 = in_4 < 1 or in_2 == 0
result_6 = in_4 != 15 or in_1 >=25
result_7 = not in_1 == 15
result_8 = not in_4 < 30 and in_2 == 0
result_9 = not in_1 != 5 and in_3 > 0
result_10 = not in_1 == 5 or not in_3 <= 10

r_l =[result_1,result_2,result_3,result_4,result_5,result_6,result_7,result_8,result_9,result_10]
for i in r_l:
    print('result =', i)



print('Введите число:')
a = int(input())

if a < 30:
    print('Вы ввели число =', a, ',', 'которое меньше 30')
elif a > 30:
    print('Вы ввели число =', a, ',', 'которое больше 30')
else:
    print('Вы ввели число =', a, ',', 'которое равно 30')



print('Введите число:')
b = int(input())

import random
n = random.randint(1, 100)

if b == n:
    print('Вы ввели число =', b, ',', 'которое равно сгенерированному числу')
elif b > n:
    print('Вы ввели число =', b, ',', 'которое больше сгенерированного числа')
else:
    print('Вы ввели число =', b, ',', 'которое меньше сгенерированного числа')

print('Сгенерированное число =', n)



print('Введите число:')
x = int(input())

import random
y_1 = random.randint(1, 100)
y_2 = random.randint(1, 100)

if y_1 < y_2:
    if x < y_1:
        print('Вы ввели число =', x, ',', 'которое меньше сгенерированных чисел y_1 и y_2')
    elif x > y_1 and x < y_2:
        print('Вы ввели число =', x, ',', 'которое больше сгенерированного числа y_1 и меньше сгенерированного числа y_2')
    elif x == y_1:
        print('Вы ввели число =', x, ',', 'которое равно сгенерированному числу y_1 и меньше сгенерированного числа y_2')
    elif x == y_2:
        print('Вы ввели число =', x, ',', 'которое больше сгенерированного числа y_1 и равно сгенерированному числу y_2')
    else:
        print('Вы ввели число =', x, ',', 'которое больше сгенерированных чисел y_1 и y_2')
elif y_1 > y_2:
    if x < y_2:
        print('Вы ввели число =', x, ',', 'которое меньше сгенерированных чисел y_1 и y_2')
    elif x < y_1 and x > y_2:
        print('Вы ввели число =', x, ',', 'которое меньше сгенерированного числа y_1 и больше сгенерированного числа y_2')
    elif x == y_2:
        print('Вы ввели число =', x, ',', 'которое меньше сгенерированного числа y_1 и равно сгенерированному числу y_2')
    elif x == y_1:
        print('Вы ввели число =', x, ',', 'которое равно сгенерированному числу y_1 и больше сгенерированного числа y_2')
    else:
        print('Вы ввели число =', x, ',', 'которое больше сгенерированных чисел y_1 и y_2')

else:
    print('Вы ввели число =', x, ',', 'которое равно сгенерированным числам y_1 и y_2')

print('Сгенерированное число y_1 =', y_1)
print('Сгенерированное число y_2 =', y_2)