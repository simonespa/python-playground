import numpy as np

# (i-1, j-1)  |  (i-1, j)  |  (i-1, j+1)
# (i, j-1)    |  (i, j)    |  (i, j+1)
# (i+1, j-1)  |  (i+1, j)  |  (i+1, j+1)
def has_same_number_of_trees(matrix, i, j):
    i_start = max(0, i - 1)
    i_stop = min(matrix.shape[0] - 1, i + 1)
    j_start = max(0, j - 1)
    j_stop = min(matrix.shape[1] - 1, j + 1)

    total_trees = 0

    for x in range(i_start, i_stop + 1):
        for y in range(j_start, j_stop + 1):
            if x == i and y == j:
                continue

            if matrix[x][y] == "*":
                total_trees += 1

    if total_trees == int(matrix[i][j]):
        return True
    else:
        return False


def houses_and_trees(matrix, A):
    N, M = matrix.shape

    total_trees = 0

    for i in range(N):

        trees_in_a_row = 0
        houses_in_a_row = 0

        for j in range(M):
            cell = matrix[i][j]
            if cell == "*":
                trees_in_a_row += 1
            else:
                house = int(cell)
                if house > 0:
                    houses_in_a_row += 1
                    if not (has_same_number_of_trees(matrix, i, j)):
                        return False

        # in each row there are more houses than trees
        if trees_in_a_row >= houses_in_a_row:
            return False

        total_trees += trees_in_a_row

    # The total number of trees must be equal to A
    if total_trees == A:
        return True
    else:
        return False
