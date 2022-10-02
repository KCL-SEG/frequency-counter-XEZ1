"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    #count = 0
    #for i in items:
    #    for j in items:
    #        if i == j:
    #            count += 1
    #    frequencies[i] = count
    #    for k in range(count):
    #        items.remove(i)
    #   count = 0

    for i in range(len(items)):
        if type(items[i]) != str:
            items[i] = str(items[i])

    for i in range(len(items)):
        frequencies[items[i]] = items.count(items[i])
        for j in range(items.count(i)):
            items.remove(i)

    return frequencies
