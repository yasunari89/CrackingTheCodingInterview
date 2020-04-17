import math
import numpy as np
from pprint import pprint

def rotate(square_matrix):
    # This function destroys the square_matrix for saving the memory.
    n = len(square_matrix)
    for i in range(math.floor(n/2)):
        for j in range(math.ceil(n/2)):
            temp = square_matrix[i][j]
            square_matrix[i][j] = square_matrix[n-j-1][i]
            square_matrix[n-j-1][i] = square_matrix[n-i-1][n-j-1]
            square_matrix[n-i-1][n-j-1] = square_matrix[j][n-i-1]
            square_matrix[j][n-i-1] = temp 


if __name__ == "__main__":
    for n in range(25):
        square_matrix = np.random.randint(0, 2, (n,n))
        ans = np.rot90(square_matrix, 3).copy()
        rotate(square_matrix)
        print((square_matrix == ans).all())
