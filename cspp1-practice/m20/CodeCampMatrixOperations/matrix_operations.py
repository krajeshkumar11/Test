"""
    Perform Matrix addition and multiplication.
"""

def mult_matrix(matrix_1, matrix_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    m_matrix_1 = len(matrix_1)
    n_matrix_1 = len(matrix_1[0])
    for each in matrix_1:
        if n_matrix_1 < len(each):
            n_matrix_1 = len(each)
    m_matrix_2 = len(matrix_2)
    n_matrix_2 = len(matrix_2[0])
    for each in matrix_2:
        if n_matrix_2 < len(each):
            n_matrix_2 = len(each)

    result_matrix = [0] * m_matrix_1
    for i in range(n_matrix_2):
        result_matrix[i] = [0] * n_matrix_2

    if n_matrix_1 == m_matrix_2:

        for i in range(m_matrix_1):
            for j in range(n_matrix_2):
                for k in range(m_matrix_2):
                    result_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]

        return result_matrix
    else:
        print('Error: Matrix shapes invalid for mult')

def add_matrix(matrix_1, matrix_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    m_matrix_1 = len(matrix_1)
    n_matrix_1 = len(matrix_1[0])
    for each in matrix_1:
        if n_matrix_1 < len(each):
            n_matrix_1 = len(each)
    m_matrix_2 = len(matrix_2)
    n_matrix_2 = len(matrix_2[0])
    for each in matrix_2:
        if n_matrix_2 < len(each):
            n_matrix_2 = len(each)

    result_matrix = [0] * m_matrix_1
    for i in range(m_matrix_1):
        result_matrix[i] = [0] * n_matrix_1

    if m_matrix_1 == m_matrix_2 and n_matrix_1 == n_matrix_2:
        for i in range(m_matrix_1):
            for j in range(n_matrix_1):
                result_matrix[i][j] = matrix_1[i][j] + matrix_2[i][j]
        return result_matrix
    else:
        print('Error: Matrix shapes invalid for addition')

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    new_matrix_size = input().split(',')
    new_matrix_size = list(map(int, new_matrix_size))

    rows_m = new_matrix_size[0]
    columns_n = new_matrix_size[1]

    new_matrix = [0] * rows_m

    for i in range(rows_m):
        new_matrix[i] = [0] * columns_n
    flag = True
    for i in range(new_matrix_size[0]):
        row_data = input().split(' ')
        row_data = list(map(int, row_data))
        if len(row_data) != new_matrix_size[1]:
            flag = False
            break
        for j in range(new_matrix_size[1]):
            new_matrix[i][j] = row_data[j]

    if not flag:
        return False
    else:
        return new_matrix


def main():
    """
        read inputs from user and perform matrix addition and multiplication for given matrices
    """
    # read matrix 1
    matrix_1 = read_matrix()
    # read matrix 2
    matrix_2 = read_matrix()

    if matrix_1 == False or matrix_2 == False:
        print('Error: Invalid input for the matrix')
    else:
        # add matrix 1 and matrix 2
        print(add_matrix(matrix_1, matrix_2))
        # multiply matrix 1 and matrix 2
        print(mult_matrix(matrix_1, matrix_2))

if __name__ == '__main__':
    main()
