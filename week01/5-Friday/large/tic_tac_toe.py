from copy import deepcopy

def move(board, location, player):
    row = location[0]
    column = location[1]
    board[row][column] = player
    return board

original_board = [[" ", " ", " "],
                  [" ", " ", " "],
                  [" ", " ", " "]]
testlist = [1, 2, 3, 4, 5]
new_board = deepcopy(original_board)
location = (1, 2)
player = "X"

newboard = move(new_board, location, player)
print(f"[{original_board[0]},\n {original_board[1]}\n {original_board[2]}]")
print(f"[{newboard[0]},\n {newboard[1]}\n {newboard[2]}]")
















    # if not isValidBoard(board):
    #     raise Exception("Board is incorrect size.")
    # if not isLocationValid(location):
    #     raise Exception("Location is not valid.")
    # if isLocationOccupied(location):
    #     raise Exception("Location is already occupied.")
    # if player != "X" or player != "Y":
    #     raise Exception("")