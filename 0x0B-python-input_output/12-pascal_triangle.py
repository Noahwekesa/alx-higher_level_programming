#!/usr/bin/python3
"""Technical Interview Preparation: Pascal's Triangle"""


def pascal_triangle(n):
    """function method question"""
    if n <= 0:
        return []
    
    triangle = []
    
    for rowIndex in range(n):
        row = []
        
        for i in range(rowIndex + 1):
            if i == 0 or i == rowIndex:
                row.append(1)
            else:
                element = row[i-1] * (rowIndex - i + 1) // i
                row.append(element)
        
        triangle.append(row)
    
    return triangle
