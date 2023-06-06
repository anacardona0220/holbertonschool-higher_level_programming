#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_1 = []
    if not sentence:
        tuple_1 = len(sentence), None
        return tuple_1
    else:
        tuple_1 = len(sentence), sentence[0]
        return (tuple_1)
