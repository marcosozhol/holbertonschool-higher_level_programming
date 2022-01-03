#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = list(tuple_a)
    if len(tuple_1) < 2:
        for i in range(len(tuple_1), 2):
            tuple_1.append(0)

    tuple_2 = list(tuple_b)
    if len(tuple_2) < 2:
        for i in range(len(tuple_2), 2):
            tuple_2.append(0)

    new_tuple = tuple([tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]])
    return new_tuple
