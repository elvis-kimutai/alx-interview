#!/usr/bin/python3
'''
function with Pascal's triangle
'''


def pascal_triangle(n):
    '''
    returns  list of lists of integers representing
    Pascal's triangle of a given integer
    '''
    plt = []
    if type(n) is not int or n <= 0:
        return plt
    for x in range(n):
        ct = []
        for y in range(x+1):
            if y == 0 or y == x:
                ct.append(1)
            else:
                ct.append(plt[x-1][y]+plt[x-1][y-1])
        plt.append(ct)
    return plt
