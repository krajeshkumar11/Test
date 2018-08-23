def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    # print('MULTIPLICATION: ', m1, m2)
    size_m1 = len(m1)
    size_n1 = len(m1[0])
    size_m2 = len(m2)
    size_n2 = len(m2[0])
        #m/n : m1/n2
    result = [0] * size_m1
    for i in range(size_m1):
        result[i] = [0] * size_n2

    if size_n1 == size_m2:
        for i in range(size_m1):
            for j in range(size_n2):
                for k in range(size_m2):
                    result[i][j] += m1[i][k] * m2[k][j]

        return result
    else:
        print('Error: Matrix shapes invalid for mult')

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    try:
        result = [0] * m
        for each in range(m):
            result[each] = [0] * n

        for i in range(m):
            for j in range(n):
                result[i][j] = m1[i][j] + m2[i][j]

        return result
    except:
        print('Error: Matrix shapes invalid for addition')

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    try:
        dim_str = input().split(',')
        global m
        m = int(dim_str[0])
        global n
        n = int(dim_str[1])

        matrix = [0] * m
        for each in range(m):
            matrix[each] = [0] * n

        for i in range(m):
            row_str = input().split(' ')
            # print(row_str)
            row_str = list(map(int, row_str))
            # print(row_str)
            for j in range(n):
                matrix[i][j] = row_str[j]
        return matrix
    except:
        print('Error: Invalid input for the matrix')
        return False

def main():
    # read matrix 1
    matrix_1 = read_matrix()
    # print(matrix_1)
    # read matrix 2
    matrix_2 = read_matrix()

    if matrix_1 != False and matrix_2 != False:
        # print(matrix_2)
        # add matrix 1 and matrix 2
        print(add_matrix(matrix_1, matrix_2))
        # multiply matrix 1 and matrix 2
        print(mult_matrix(matrix_1, matrix_2))

if __name__ == '__main__':
    main()
