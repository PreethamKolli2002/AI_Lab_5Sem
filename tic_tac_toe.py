
board = [['_','_','_'],['_','_','_'],['_','_','_']]
map_values = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}
players = {1:'X',2:'O'}

def check_row(player):
    for i in range(0,3):
        count_row=0
        for j in range(0,3):
            if board[i][j] == players[player]:
                count_row+=1
        if count_row==3:
            return True
    
    return False

def check_column(player):
    for j in range(0,3):
        count_col=0
        for i in range(0,3):
            if board[i][j] == players[player]:
                count_col+=1
        if count_col==3:
            return True
    
    return False

def check_diag(player):
    if(board[0][0]==board[1][1]==board[2][2]==players[player] or board[0][2]==board[1][1]==board[2][0]==players[player]):
        return True
    else:
        return False

def update_board(place,val):
    i=map_values[place][0]
    j=map_values[place][1]
    if(board[i][j]=='_'):
        board[i][j]=val
        return True
    else:
        return False

def print_board(board):
    for i in range(0,3):
        for j in range(0,3):
            print(board[i][j],end="  ")
        print()
        print()


def main_logic():
    print("Welcome to tic-tac-toe!")
    print_board(board)

    available_player = 1
    ct_board=0

    while True:
        l1 = int(input(f'Enter input(1-9) , User {available_player}: '))
        update_board(l1,players[available_player])
        print_board(board)
        if(check_row(available_player) or check_column(available_player) or check_diag(available_player)):
            print("Yayy!! User ",available_player," won!!")
            break
        else:
            available_player=2
            ct_board+=1

        if ct_board==9:
            print("Oops! Draw! Exiting...")
            break
        
        l2 = int(input(f'Enter input(1-9) , User {available_player}: '))
        update_board(l2,players[available_player])
        print_board(board)
        if(check_row(available_player) or check_column(available_player) or check_diag(available_player)):
            print("Yayy!! User ",available_player," won!!")
            break
        else:
            available_player=1
            ct_board+=1

        if ct_board==9:
            print("Oops! Draw! Exiting...")
            break


main_logic()
