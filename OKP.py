import numpy as np


class OKP(object):
    player_num: int

    def __init__(self, player_num=2, test=None):
        if test is None:
            self.player_num = player_num
            self.player_names = [None] * player_num
            self.add_players()
        else:
            self.player_num = 2
            self.player_names = ['A', 'B']

        self.game_board = np.ones((self.player_num, 5))
        self.row_pointer = None
        self.col_pointer = None
        self.rc = None
        self.num = None

    def add_players(self):
        for i in range(self.player_num):
            print(f"Enter Member {i + 1}")
            self.player_names[i] = input()

    def get_player_list(self):
        return self.player_names

    def get_board(self):
        return self.game_board

    def check_game(self):
        for i in range(self.player_num):
            count = 0
            for j in range(5):
                if self.game_board[i][j] == 0:
                    count += 1
            if count == 5:
                return True
        return False

    def karakk(self, num, rc):

        is_counting = True
        count = 0
        self.num = num
        self.rc = rc
        while is_counting:
            self.col_pointer += 1
            if self.col_pointer > 4:
                self.col_pointer = 0
                self.row_pointer += 1
                if self.row_pointer >= self.player_num:
                    self.row_pointer = 0
            if self.game_board[self.row_pointer, self.col_pointer] == 1:
                count += 1
            if count == 13:
                is_counting = False
        if self.rc == 'r':
            return self.row_pointer
        else:
            return self.col_pointer

    def start_game(self):
        self.row_pointer = 0
        self.col_pointer = 0
        winner = ''
        self.add_players()
        self.get_player_list()
        print(self.get_board())
        game_end = False
        while not game_end:
            r = self.row_pointer
            # 13 is taken as the number of open fingers to be moved each time Oramma is evoked.
            self.row_pointer = self.karakk(13, 'r')
            self.col_pointer = self.karakk(13, 'c')
            print("Oramma kadayil poyi, \nOru dazan vala vaangi, \nAa valayude niramenth?")
            print(f"{self.player_names[self.row_pointer]}:")
            c = input()
            r = self.row_pointer
            self.row_pointer = self.karakk(len(c), 'r')
            self.col_pointer = self.karakk(len(c), 'c')
            self.game_board[self.row_pointer, self.col_pointer] = 0
            print(self.get_board())
            game_end = self.check_game()
            winner = self.player_names[self.row_pointer]  # winner will be printed only after while loop is break
            r = row_pointer
            row_pointer = self.karakk(1, 'r')
            self.col_pointer = self.karakk(1, 'c')
        print(f'Winner is {winner}')


new_game = OKP()
