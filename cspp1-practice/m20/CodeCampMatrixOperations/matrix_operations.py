import numpy

def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    mm1 = len(m1)
    nm1 = len(m1[0])
    for each in m1:
        if nm1 < len(each):
            nm1 = len(each)
    mm2 = len(m2)
    nm2 = len(m2[0])
    for each in m2:
        if nm2 < len(each):
            nm2 = len(each)

    if nm1 == mm2:
        result_matrix = range(nm1 * mm2)

        result_matrix = reshape(result_matrix,(nm1, mm2))

        # result_matrix = [0] * mm1
        # for i in range(mm2):
        #     result_matrix[i] = [0] * mm2
        for i in range(mm1):
            for j in range(nm2):
                for k in range(mm2):
                    result_matrix[i][j] += m1[i][k] * m2[k][j]

        return result_matrix
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
    mm1 = len(m1)
    nm1 = len(m1[0])
    for each in m1:
        if nm1 < len(each):
            nm1 = len(each)
    mm2 = len(m2)
    nm2 = len(m2[0])
    for each in m2:
        if nm2 < len(each):
            nm2 = len(each)

    if mm1 == mm2 and nm1 ==nm2:
        result_matrix = [0] * mm1
        for i in range(mm1):
            result_matrix[i] = [0] * nm1
        for i in range(mm1):
            for j in range(nm1):
                result_matrix[i][j] = m1[i][j] + m2[i][j]
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

    m = new_matrix_size[0]
    n = new_matrix_size[1]

    new_matrix = [0] * m

    for i in range(m):
        new_matrix[i] = [0] * n
    flag = True
    for i in range(new_matrix_size[0]):
        row_data = input().split(' ')
        row_data = list(map(int, row_data))
        if len(row_data) != new_matrix_size[1]:
            flag = False
            break
        for j in range(new_matrix_size[1]):
            new_matrix[i][j] = row_data[j]

    if not flag :
        return False
    else:
        return new_matrix


def main():
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
