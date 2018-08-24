
# def vt_winner(matrix):

#     for i in range(num_rows):
#         count_x = 0
#         count_o = 0
#         for j in range(num_rows):
#             if matrix[j][i] == 'x':
#                 count_x += 1
#             elif matrix[j][i] == 'o':
#                 count_o += 1
#         print(count_x, count_o)
#         if count_x == 3:
#             print('x')
#         elif count_o == 3:
#             print('o')

# def rl_diagonal(matrix):
#     j = num_rows - 1
#     count_x = 0
#     count_o = 0
#     for i in range(num_rows):
#         if matrix[i][j] == 'x':
#             count_x += 1
#         elif matrix[i][j] == 'o':
#             count_o += 1
#         j -= 1

#     if count_x == 3:
#         print('x')
#     elif count_o == 3:
#         print('o')

def lr_rl_diagonal(matrix, pattern):
    count_x = 0
    count_o = 0
    j = num_rows - 1
    for i in range(num_rows):
        if pattern == 'LR':
            if matrix[i][i] == 'x':
                count_x += 1
            elif matrix[i][i] == 'o':
                count_o += 1
        elif pattern == 'RL':
            if matrix[i][j] == 'x':
                count_x += 1
            elif matrix[i][j] == 'o':
                count_o += 1
            j -= 1

    if count_x == 3:
        # print('x')
        return (True, 'x')
    elif count_o == 3:
        # print('o')
        return (True, 'o')
    else:
        return (False, 'draw')


def hz_vt_winner(matrix, patter):
    # print(matrix)
    flag_x = False
    flag_o = False
    for i in range(num_rows):
        count_x = 0
        count_o = 0
        for j in range(num_rows):
            if patter == 'HZ':
                if matrix[i][j] == 'x':
                    count_x += 1
                elif matrix[i][j] == 'o':
                    count_o += 1
            elif patter == 'VT':
                if matrix[j][i] == 'x':
                    count_x += 1
                elif matrix[j][i] == 'o':
                    count_o += 1
        # print(count_x, count_o)
        if count_x == 3:
            flag_x = True
        elif count_o == 3:
            flag_o = True

    if flag_x:
        # print('x')
        return (True, 'x')
    elif flag_o:
        # print('o')
        return (True, 'o')
    else:
        # print('draw')
        return (False, 'draw')

def game_validation(matrix):
    count_x = 0
    count_o = 0

    for i in matrix:
        for j in i:
            if j == 'x':
                count_x += 1
            elif j == 'o':
                count_o += 1

    if abs(count_x - count_o) == 1:
        return True
    return False


def data_validation(matrix):
    valid_data = ['x', 'o', '.']
    for i in matrix:
        for j in i:
            if j not in valid_data:
                return False
    return True

def main():
    global num_rows
    num_rows = 3
    matrix = []
    for i in range(num_rows):
        user_input = input().split(' ')
        matrix.append(user_input)

    if game_validation(matrix):
        if data_validation(matrix):
            result_list = list(hz_vt_winner(matrix, 'HZ'))
            if result_list[0]:
                print(result_list[1])
                return
            result_list = list(hz_vt_winner(matrix, 'VT'))
            if result_list[0]:
                print(result_list[1])
                return
            result_list = list(lr_rl_diagonal(matrix, 'LR'))
            if result_list[0]:
                print(result_list[1])
                return
            result_list = list(lr_rl_diagonal(matrix, 'RL'))
            if result_list[0]:
                print(result_list[1])
                return
            print('draw')
            return
        else:
            print('invalid input')
            return
    else:
        print('invalid game')
        return

if __name__ == '__main__':
    main()
