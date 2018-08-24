
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
        print('x')
    elif count_o == 3:
        print('o')
    else:
        print('draw')

def hz_vt_winner(matrix, patter):
    # print(matrix)
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
            print('x')
            return True
        elif count_o == 3:
            print('o')
            return True
        else:
            print('draw')
            return True


def main():
    global num_rows
    num_rows = 3
    matrix = []
    for i in range(num_rows):
        user_input = input().split(' ')
        matrix.append(user_input)

    result = hz_vt_winner(matrix, 'HZ')
    if result == False:
        result = hz_vt_winner(matrix, 'VT')
        if result == False:
            result = lr_rl_diagonal(matrix, 'LR')
        else:
            result = lr_rl_diagonal(matrix, 'RL')

if __name__ == '__main__':
    main()
