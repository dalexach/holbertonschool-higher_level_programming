#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    leng = len(sys.argv)
    if leng == 1:
        print('{} arguments.'.format(leng - 1))
    elif len(sys.argv) == 2:
        print('{} argument:'.format(leng - 1))
    else:
        print('{} arguments:'.format(leng - 1))
    for i in range(leng):
        if i == 0:
            continue
        print('{:d}: {:s}'.format(i, sys.argv[i]))
