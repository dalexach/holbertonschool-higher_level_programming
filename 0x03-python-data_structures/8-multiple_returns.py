#!/usr/bin/python3


def multiple_returns(sentence):
    leng = len(sentence)
    if leng == 0:
        first_ch = None
    else:
        first_ch = sentence[0]
    return (leng, first_ch)
