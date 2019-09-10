#!/usr/bin/python3
def fizzbuzz():
    str1 = 'Fizz'
    str2 = 'Buzz'
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('{:s}'.format(str1 + str2), end=' ')
        elif i % 3 == 0 and i % 5 != 0:
            print('{:s}'.format(str1), end=' ')
        elif i % 3 != 0 and i % 5 == 0:
            print('{:s}'.format(str2), end=' ')
        else:
            print('{}'.format(i), end=' ')
        if i == 100:
            print(end='')
