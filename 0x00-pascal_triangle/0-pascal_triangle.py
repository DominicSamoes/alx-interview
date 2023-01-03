#!/usr/bin/python3
"""
Function returns a list of integers representing the Pascal’s triangle of n
"""

def pascal_triangle(n):
    """
    Creates list of ints representing Pascal's triangle

    Parameters:
        n:
        The number of rows of Pascal's triangle to be created

    return:
        list of ints:
            Represents Pascal's triangle
    """
    if type(n) is not int:
        raise TypeError("n must be an integer")
    pascal_triangle = []
    if n <= 0:
        return pascal_triangle
    prev = [1]
    for i in range(n):
        i_list = []
        if i == 0:
            i_list = [1]
        else:
            for j in range(i + 1):
                if j == 0:
                    i_list.append(0 + prev[j])
                elif j == i:
                    i_list.append(prev[j - 1] + 0)
                else:
                    i_list.append(prev[j - 1] + prev[j])
        prev = i_list
        pascal_triangle.append(i_list)
    return pascal_triangle
