#!/usr/bin/python3
"""
A module to define a method for Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Represent Pascal's Triangle of size n.
    :param n: number of rows
    :return:  list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
