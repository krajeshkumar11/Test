
def game_validate():
    pass

def input_validate():
    pass

def lr_diagonal(game_data, side):
    player_1 = False
    player_2 = False
    # print(game_data)
    count_x = 0
    count_o = 0
    if side == 'LR':
        for i in range(len(game_data)):
            if game_data[i][i] == 'x':
                count_x += 1
            elif game_data[i][i] == 'o':
                count_o += 1
    elif side == 'RL':
        j = len(game_data) - 1
        i = 0
        while j >= 0:
            if game_data[i][j] == 'x':
                count_x += 1
            elif game_data[i][j] == 'o':
                count_o += 1
            i += 1
            j -= 1

    if count_x == 3:
        player_1 = True
    if count_o == 3:
        player_2 = True

    if player_1 and player_2:
        return (True, 'draw')
    elif player_1:
        return (True, 'x')
    elif player_2:
        return (True, 'o')
    else:
        return (False, '')

def hor_ver_winner(game_data, side):
    player_1 = False
    player_2 = False
    # print(game_data)
    for i in range(len(game_data)):
        count_x = 0
        count_o = 0
        for j in range(len(game_data[i])):
            if side == 'HZ':
                if game_data[i][j] == 'x':
                    count_x += 1
                elif game_data[i][j] == 'o':
                    count_o += 1
            elif side == 'VT':
                if game_data[j][i] == 'x':
                    count_x += 1
                elif game_data[j][i] == 'o':
                    count_o += 1
        if count_x == 3:
            player_1 = True
        if count_o == 3:
            player_2 = True

    if player_1 and player_2:
        return (True, 'draw')
    elif player_1:
        return (True, 'x')
    elif player_2:
        return (True, 'o')
    else:
        return (False, '')

def game_winner(game_data):
    # Horizontal Check
    result_data = list(hor_ver_winner(game_data, 'HZ'))
    if result_data[0] == True:
        return result_data[1]
    # Vertical Check
    result_data = list(hor_ver_winner(game_data, 'VT'))
    if result_data[0] == True:
        return result_data[1]
    # Diagonal Left to Right
    result_data = list(lr_diagonal(game_data, 'LR'))
    if result_data[0] == True:
        return result_data[1]
    # Diagonal Right to Left
    result_data = list(lr_diagonal(game_data, 'RL'))
    if result_data[0] == True:
        return result_data[1]

def main():
    num_rows = 3
    game_data = ['0'] * num_rows
    for i in range(num_rows):
        game_data[i] = ['0'] * num_rows
    # print(game_data)
    for i in range(num_rows):
        rows = input().split(' ')
        for j in range(num_rows):
            game_data[i][j] = rows[j]
    # print(game_data)
    print(game_winner(game_data))

if __name__ == '__main__':
    main()
