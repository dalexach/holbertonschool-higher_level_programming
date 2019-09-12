#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    leng = len(sys.argv)
    sum = 0
    for i in range(leng):
        if i == 0:
            continue
        sum += int(sys.argv[i])
    print('{}'.format(sum))
