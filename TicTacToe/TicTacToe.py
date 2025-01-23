import random

def print_game_board(game_board):
    for row in game_board:
        print("".join(row))

def design_piece(game_board, user_input, user):
    symbol = ' '
    if user == "player":
        symbol = 'X'
        player_movements.append(user_input)
    elif user == "computer":
        symbol = 'O'
        computer_movements.append(user_input)

    mapping = {
        1: (0, 0), 2: (0, 2), 3: (0, 4),
        4: (2, 0), 5: (2, 2), 6: (2, 4),
        7: (4, 0), 8: (4, 2), 9: (4, 4)
    }
    x, y = mapping[user_input]
    game_board[x][y] = symbol

def check_winner():
    winning = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    for win in winning:
        if all(move in player_movements for move in win):
            return "Congratulations you won!"
        elif all(move in computer_movements for move in win):
            return "Computer wins!"
    if len(player_movements) + len(computer_movements) == 9:
        return "Good the game is a draw!"
    return ""

game_board = [
    [' ', '|', ' ', '|', ' '],
    ['-', '+', '-', '+', '-'],
    [' ', '|', ' ', '|', ' '],
    ['-', '+', '-', '+', '-'],
    [' ', '|', ' ', '|', ' ']
]

player_movements = []
computer_movements = []

print_game_board(game_board)

while True:  
    user_input = int(input("Enter your input (1-9): "))
    while user_input in player_movements or user_input in computer_movements:
        print("Movement taken! Please enter another movement")
        user_input = int(input("Enter your input (1-9): "))
    
    design_piece(game_board, user_input, "player")

    computer_input = random.randint(1, 9)
    while computer_input in player_movements or computer_input in computer_movements:
        computer_input = random.randint(1, 9)
    
    design_piece(game_board, computer_input, "computer")
    print_game_board(game_board)

    result = check_winner()
    if result:
        print(result)
        break
