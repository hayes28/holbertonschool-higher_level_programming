#!/usr/bin/python3
"""Pascal's Triangle-
Technical interview preparation: """


def pascal_triangle(n):
    """ Returns list of Pascal's Triangle """
    triangle = []
    for i in range(n):
        triangle.append([])
        for j in range(i + 1):
            if j in [i, 0]:
                triangle[i].append(1)
            else:
                triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    return triangle
