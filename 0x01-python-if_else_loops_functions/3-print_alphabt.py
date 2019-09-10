#!/usr/bin/python3
i = 0
while i < 26:
    if i == 4 or i == 16:
        i += 1
    else:
        print('{:c}'.format(i + 97), end='')
    i += 1
