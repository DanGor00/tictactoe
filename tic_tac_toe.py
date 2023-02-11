import random
import time

def init_board():
    board = [ [ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ] ]
    return board

def convert_player(player):
    if player == "X":
        return "0"
    if player == "0":
        return "X"

def letters_to_numbers(letter):
    if letter == "A":
        return 0
    elif letter == "B":
        return 1
    elif letter == "C":
        return 2

def get_player_move(board):
    row, col = 0, 0
    while True:
        player_input = input("Type coordinates in example A2 means first row and second column. There are 3 rows and 3 columns: ").upper().strip()
        if player_input == "QUIT":
            exit()
        #player_input = list(player_input)
        if player_input[0] in ["A","B","C"] and player_input[1] in ["1","2","3"]:
            player_input_row = letters_to_numbers(player_input[0])
            player_input_col = int(player_input[1])-1
            if board[player_input_row][player_input_col] == '.':
                break
            else:
                print("Chosen coordinates are already taken!")
                continue
        else:
            print("Choose valid coordinates! Rows beetween A-C and columns beetween 1-3")
    row = player_input[0]
    col = player_input[1]
    return row, col

def get_ai_move(board,player):
    if is_full(board) == False:
        return None
    board ,var = find_win_move(board,player)
    if var == False:
        board ,var = prevent_win_move(board,player)
    if is_full(board) == True and var == False:
        while True:
            abc = random.randint(0,2)
            jdt = random.randint(0,2)
            member=board[abc][jdt]
            if member == ".":
                board[abc][jdt] = player
                return board

def get_exp_ai_move(board,player):
    if not is_full(board):
        return None
    if board[1][1] == ".":
        board[1][1] = player
        return board, player
    count_0 = str(board).count("0")
    if count_0 == 1:
        if board[0][0] == "0":
            board[2][2] = player
            return board, player
        if board[0][2] == "0":
            board[2][0] = player
            return board, player
        if board[2][0] == "0":
            board[0][2] = player
            return board, player
        if board[2][2] == "0":
            board[0][0] = player
            return board, player
    get_ai_move(board, player)

#podstawić 
def mark(board, player, row, col):
    if row == "A":
        row = 0
    elif row =="B":
        row = 1
    else:
        row = 2
    col = int(col) - 1
    board[row][col] = player
    return board    

def has_won(board, player):
    for i in range(len(list(board))):
        if list(board[i]) == list([player] + [player] + [player]):
            return True
    for i in range(len(list(board))):
            if list([board[0][i]]+[board[1][i]]+[board[2][i]]) == list([player] + [player] + [player]):
                return True
    if list(board[0][0] + board[1][1] + board [2][2]) == list([player] + [player] + [player]):
        return True
    elif list(board[0][2] + board[1][1] + board [2][0]) == list([player] + [player] + [player]):
        return True
    else:
        return False

#pod for konwersja
def prevent_cross_win_move(board,player):
    winbord =[[player,player,'.'],[player,'.',player],['.',player,player]]
    for row in range(3):
        if [board[0][0],board[1][1],board[2][2]] == winbord[row]:
            player = convert_player(player)
            for i in range(3):
                if board[i][i] == '.':
                    board[i][i] = player
                    return board ,True
        elif [board[0][2],board[1][1],board[2][0]] == winbord[row]:
            player = convert_player(player)
            if board[0][2] == '.':
                board[0][2] = player
                return board ,True
            if board[1][1] == '.':
                board[1][1] = player
                return board ,True
            if board[2][0] == '.':
                board[2][0] = player
                return board ,True
    return board ,False

def prevent_win_move(board,player):
    player = convert_player(player)
    winbord =[[player,player,'.'],[player,'.',player],['.',player,player]]
    for row in range(3):
        for col in range(3):
            if board[row] == winbord[col]:
                player = convert_player(player)
                for i in range(3):
                    if board[row][i] == '.':
                        board[row][i] = player
                        return board ,True
    for col in range(3):
        for row in range(3):
            if [board[0][col],board[1][col],board[2][col]] ==  winbord[row]:
                player = convert_player(player)
                for i in range(3):
                    if board[i][col] == '.':
                        board[i][col] = player
                        return board ,True
    return prevent_cross_win_move(board,player)
#...
def find_win_move(board,player):
    winbord =[[player,player,'.'],[player,'.',player],['.',player,player]]
    for row in range(3):
        for col in range(3):
            if board[row] == winbord[col]:
                board[row] = [player,player,player]
                return board ,True
    for col in range(3):
        for row in range(3):
            if [board[0][col],board[1][col],board[2][col]] ==  winbord[row]:
                [board[0][col],board[1][col],board[2][col]] = [player,player,player]
                return board ,True
            if [board[0][0],board[1][1],board[2][2]] == winbord[row]:
                [board[0][0],board[1][1],board[2][2]] = [player,player,player]
                return board ,True
            elif [board[0][2],board[1][1],board[2][0]] == winbord[row]:
                [board[0][2],board[1][1],board[2][0]] = [player,player,player]
                return board ,True
        return board ,False
#...
def is_full(board):
    dot = 0
    for i in range(len(board)):
        for x in range(len(board)):
            if "." in board[i][x]:
               return True
    return False

def print_board(board):
    print('   1   2   3')
    print('A  '+ board[0][0] +' | '+ board[0][1] +' | '+ board[0][2])
    print('  ---+---+---')
    print('B  '+ board[1][0] +' | '+ board[1][1] +' | '+ board[1][2])
    print('  ---+---+---')
    print('C  '+ board[2][0] +' | '+ board[2][1] +' | '+ board[2][2])

def print_result(winner,board):
    if winner == "X":
        print("X has won!")
        print_board(board)
    elif winner == "0":
        print("0 has won!")
        print_board(board)
    else:
        print("It's a tie!")
        print_board(board)
#
def mode_human_human(board):
    player = "X"
    while has_won(board,player) == False and is_full(board) == True:
        print_board(board)
        player = "X"
        print("Player X turn")
        row, col = get_player_move(board)
        mark(board, player, row, col)
        if has_won(board,player) == False and is_full(board) == True:
            player = "0"
            print_board(board)
            print("Player 0 turn")
            row, col = get_player_move(board)
            mark(board, player, row, col)
            winner = player
            pass
        else:
            winner = player
    if is_full(board) == False and has_won(board,player) == False:
            winner = "TIE"
    return winner , board
#
def mode_human_ai(board):
    player = "X"
    while has_won(board,player) == False and is_full(board) == True:
        print_board(board)
        player = "X"
        print("Player X turn")
        row, col = get_player_move(board)
        mark(board, player, row, col)
        if has_won(board,player) == False and is_full(board) == True:
            player = "0"
            print_board(board)
            print("Player 0 turn")
            get_ai_move(board,player)
            winner = player
            pass
        else:
            winner = player
    if is_full(board) == False and has_won(board,player) == False:
        winner = "TIE"
    return winner , board

def mode_ai_ai(board):
    player = 'X'
    while has_won(board,player) == False and is_full(board) == True:
        player = "X"
        print_board(board)
        print("Player X turn")
        get_ai_move(board,player)
        time.sleep(1)
        winner = player
        if has_won(board,player) == False and is_full(board) == True:
            player = "0"
            print_board(board)
            print("Player 0 turn")
            get_ai_move(board,player)
            time.sleep(1)
            winner = player
            pass
        else:
                winner = player
    if is_full(board) == False and has_won(board,player) == False :
        winner = "TIE"
    return winner ,board

def mode_exp_ai(board):
    player = 'X'
    while has_won(board,player) == False and is_full(board) == True:
        player = "X"
        print_board(board)
        print("Player X turn")
        get_exp_ai_move(board,player)
        time.sleep(1)
        winner = player
        if has_won(board,player) == False and is_full(board) == True:
            player = "0"
            print_board(board)
            print("Player 0 turn")
            row, col = get_player_move(board)
            mark(board, player, row, col)
            winner = player
            pass
        else:
                winner = player
    if is_full(board) == False and has_won(board,player) == False :
        winner = "TIE"
    return winner ,board
    
def tictactoe_game(mode):
    board = init_board()
    if mode == 'HUMAN-HUMAN':
        return mode_human_human(board)       
    elif mode == 'HUMAN-AI':
        return mode_human_ai(board)      
    elif mode == 'AI-AI':
        return mode_ai_ai(board)
    elif mode == 'EXP-AI':
        return mode_exp_ai(board)
        
def main_menu():
    while True:
        mode=input('HUMAN-HUMAN press 1\nHUMAN-AI press 2\nAI-AI 3\nHUMAN-EXPERT_AI 4\n').upper()
        if mode == "1":
            winner ,board = tictactoe_game('HUMAN-HUMAN')
            print_result(winner,board)
        elif mode == "2":
            winner ,board = tictactoe_game('HUMAN-AI')
            print_result(winner,board)
        elif mode == "3":
            winner ,board = tictactoe_game('AI-AI')
            print_result(winner,board)
        elif mode == "4":
            winner ,board = tictactoe_game('EXP-AI')
            print_result(winner,board)
        elif mode == "QUIT":
            exit()
        else:
            print('Invalid mode please try again!')

if __name__ == '__main__':
    main_menu()
