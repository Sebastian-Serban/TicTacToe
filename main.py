def check_game_status(matrix):
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == 1 or matrix[0][0] == matrix[1][1] == matrix[2][2] == 2:
        return True
    elif matrix[0][2] == matrix[1][1] == matrix[2][0] == 1 or matrix[0][2] == matrix[1][1] == matrix[2][0] == 2:
        return True
    else:
        for row in matrix:
            if all(elem == row[0] == 1 for elem in row) or all(elem == row[0] == 2 for elem in row):
                return True
        for j in range(len(matrix[0])):
            column = [matrix[i][j] for i in range(len(matrix))]
            if all(elem == column[0] == 1 for elem in column) or all(elem == column[0] == 2 for elem in column):
                return True    
    return False

def check_draw(matrix):
    for x in matrix:
        if 0 in x:
            return False
    return True



def main():
    player_grid = "___|___|___ \n\
___|___|___ \n\
   |   |    \n" 
    
    coordinates_matrix = {1:[0, 0], 2:[0, 1], 3:[0, 2], 4:[1, 0], 5:[1, 1], 6:[1, 2], 7:[2, 0], 8:[2, 1], 9:[2, 2]}
    coordinates_player_grid = {1:1, 2:5, 3:9, 4:14, 5:18, 6:22, 7:27, 8:31, 9:35}
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    player = True
    player_input = 0
    while not check_game_status(matrix):
        if check_draw(matrix):
            print(player_grid)
            print("Draw!")
            return None
        else:
            print(player_grid)
            if player:
                player_input = int(input("Player 1, where do you want to put your x (coordinates: 1, 2, 3 . . .)   :   "))
                if matrix[coordinates_matrix[player_input][0]][coordinates_matrix[player_input][1]] != 0:
                    print("This place is already taken! Penalty : the other player gets another turn")
                else:
                    matrix[coordinates_matrix[player_input][0]][coordinates_matrix[player_input][1]] = 1
                    player_grid = player_grid[:coordinates_player_grid[player_input]] + "X" + player_grid[coordinates_player_grid[player_input]+1:]
                player = False
            else:
                player_input = int(input("Player 2, where do you want to put your O (coordinates: 1, 2, 3 . . .)   :   "))
                if matrix[coordinates_matrix[player_input][0]][coordinates_matrix[player_input][1]] != 0:
                        print("This place is already taken! Penalty : the other player gets another turn")
                else:
                    matrix[coordinates_matrix[player_input][0]][coordinates_matrix[player_input][1]] = 2
                    player_grid = player_grid[:coordinates_player_grid[player_input]] + "O" + player_grid[coordinates_player_grid[player_input]+1:]
                player = True
    print(player_grid)
    print(f"Player {2 if player else 1} wins!")
    return None 
main()