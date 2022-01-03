#!/usr/bin/python3
def multiple_returns(sentence):
    n = len(sentence)
    if n == 0:
        caracter = None
        return n, caracter
    else:
        caracter = sentence[0]
        return n, caracter
