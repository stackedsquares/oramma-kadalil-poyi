import numpy as np
'''
Logic for the game Orammma kadalil poyi
Don't know many inbuilt functions. It can be improved with inbuilt functions from numpy.
A repository of colours can be built so only the colours in the repository can be used as responses.
Another functionality can be built to stop same colour being given twice.
'''
def initiate():
    print ('Please enter the number of players.')
    number_of_players = input()
    n = int(number_of_players)
    players = ["" for x in range(n)]
    for p in range(n):
        print(f'Enter the name of player {p + 1}')
        players[p] = input()
    return players

def initiate_gameboard(n):
   g = np.ones((n, 5))
   return g

def print_gameboard(players, gameboard):
    for i in range(len(players)):
        print(players[i], gameboard[i])
        print('\n')

def check_game(gameboard, n):
    for i in range(n):
        count = 0
        for j in range(5):
            if gameboard[i][j] == 0:
                count += 1
        if count == 5:
            return True
    return False

# to determine how many open fingers are to be moved. Returns the col_pointer and row_pointer separately depending on value of rc variable
def karakk (gameboard, row_pointer, col_pointer, n, num, rc):
    counting = True
    count = 0
    while (counting):
        col_pointer += 1
        if (col_pointer > 4):
            col_pointer = 0
            row_pointer += 1
            if (row_pointer >= n):
                row_pointer = 0
        if gameboard[row_pointer, col_pointer] == 1:
            count += 1
        if (count == num):
            counting = False
    if rc == 'r':
        return row_pointer
    else:
        return col_pointer

def main():
    row_pointer = 0
    col_pointer = 0
    winner = ''
    players = initiate()
    gameboard = initiate_gameboard(len(players))
    print_gameboard(players, gameboard)
    game_end = False
    while(game_end==False):
        r = row_pointer
        # 13 is taken as the number of open fingers to be moved each time Oramma is evoked.
        row_pointer = karakk(gameboard, row_pointer, col_pointer, len(players), 13, 'r')
        col_pointer = karakk(gameboard, r, col_pointer, len(players), 13, 'c')
        print(f'Oramma kadayil poyi, \nOru dazan vala vaangi, \nAa valayude niramenth? {players[row_pointer]}')
        c = input()
        r = row_pointer
        row_pointer = karakk(gameboard, row_pointer, col_pointer, len(players), len(c), 'r')
        col_pointer = karakk(gameboard, r, col_pointer, len(players), len(c), 'c')
        gameboard[row_pointer, col_pointer] = 0
        print_gameboard(players, gameboard)
        game_end = check_game(gameboard, len(players))
        winner = players[row_pointer] #winner will be printed only after while loop is break
        r = row_pointer
        row_pointer = karakk(gameboard, row_pointer, col_pointer, len(players), 1, 'r')
        col_pointer = karakk(gameboard, r, col_pointer, len(players), 1, 'c')
    print (f'Winner is {winner}')

if __name__ == "__main__":
    main()