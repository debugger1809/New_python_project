Problem 
#Given a square matrix, calculate the absolute difference between the sums of #its diagonals.
#For example, the square matrix is shown below:
#1 2 3
#4 5 6
#9 8 9  
#The left-to-right diagonal = . The right to left diagonal = . Their absolute #difference is . 
#Solution: 
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonal_difference(matrix):
    matrix = []
    N = input()
    l = sum(matrix[i][i] for i in range(N))
    r = sum(matrix[i][N-i-1] for i in range(N))
    return abs(l - r)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    matrix = []
    N = input()
    for _ in range(N):
        matrix.append(map(int, raw_input().split()))

    result = diagonal_difference(matrix)
    
    fptr.write(int(result) + '\n')

    fptr.close()
