class Connect4:

    def __init__(self):
        print('hello')
        self.get_player_names()
        self.whose_go = 1
        self.there_is_a_winner = False
        self.initialise_board()

    def get_player_names(self):
        self.players = ['anna', 'peter']

    def initialise_board(self):
        n = 6
        m = 7
        self.board = [0] * n
        for i in range(n):
            self.board[i] = [0] * m

    def play(self):
        self.draw_board()
        print('Where would you like to go,', self.player_name())
        column = int(input()) - 1
        self.add_counter(column, self.whose_go)
        if self.player_has_won():
            self.draw_board()
            print(self.player_name(), ', you have defeated your opponent and now you are better than them at connect 4! you banana')
            self.there_is_a_winner = True
        else:
            self.whose_go = 2 - (self.whose_go -  1)

    def player_name(self):
        return self.players[self.whose_go - 1]

    def player_has_won(self):
        if self.counters_underneath() == 3:
            return True
        if self.counters_diagonal1() + self.counters_diagonal2() == 3:
            return True
        if self.counters_left() + self.counters_right() == 3:
            return True
        if self.counters_diagonal_downl() + self.counters_diagonal_upr() == 3:
            return True
            return True
        return False

    def counters_diagonal_downl(self):
        if self.last_row == 1:
            return 0
        if self.last_column == 1:
            return 0
        if self.board[self.last_row + 1][self.last_column - 1] != self.whose_go:
            return 0
        if self.last_row == 0:
            return 1
        if self.last_column == 1:
            return 1
        if self.board[self.last_row + 2][self.last_column - 2] != self.whose_go:
            return 1
        if self.last_row == 0:
            return 2
        if self.last_column == 2:
            return 2
        if self.board[self.last_row + 3][self.last_column - 3] != self.whose_go:
            return 2
        return 3

    def counters_diagonal_upr(self):
        if self.last_row == 0:
            return 0
        if self.last_column == 6:
            return 0
        if self.board[self.last_row - 1][self.last_column + 1] != self.whose_go:
            return 0
        if self.last_row == 1:
            return 1
        if self.last_column == 5:
            return 1
        if self.board[self.last_row - 2][self.last_column + 2] != self.whose_go:
            return 1
        if self.last_row == 2:
            return 2
        if self.last_column == 4:
            return 2
        if self.board[self.last_row - 3][self.last_column + 3] != self.whose_go:
            return 2
        return 3

    def counters_diagonal1(self):
        if self.last_row == 5:
            return 0
        if self.last_column == 6:
            return 0
        if self.board[self.last_row + 1][self.last_column + 1] != self.whose_go:
            return 0
        if self.last_row == 4:
            return 1
        if self.last_column == 5:
            return 1
        if self.board[self.last_row + 2][self.last_column + 2] != self.whose_go:
            return 1
        if self.last_row == 3:
            return 2
        if self.last_column == 4:
            return 2
        if self.board[self.last_row + 3][self.last_column + 3] != self.whose_go:
            return 2
        return 3

    def counters_diagonal2(self):
        if self.last_row == 5:
            return 0
        if self.last_column == 0:
            return 0
        if self.board[self.last_row - 1][self.last_column - 1] != self.whose_go:
            return 0
        if self.last_row == 4:
            return 1
        if self.last_column == 1:
            return 1
        if self.board[self.last_row - 2][self.last_column - 2] != self.whose_go:
            return 1
        if self.last_row == 3:
            return 2
        if self.last_column == 2:
            return 2
        if self.board[self.last_row - 3][self.last_column - 3] != self.whose_go:
            return 2
        return 3

    def counters_underneath(self):
        if self.last_row == 5:
            return 0
        if self.board[self.last_row + 1][self.last_column] != self.whose_go:
            return 0
        if self.last_row == 4:
            return 1
        if self.board[self.last_row + 2][self.last_column] != self.whose_go:
            return 1
        if self.last_row == 3:
            return 2
        if self.board[self.last_row + 3][self.last_column] != self.whose_go:
            return 2
        return 3

    def counters_left(self):
        if self.last_column == 0:
            return 0
        if self.board[self.last_row ][self.last_column - 1] != self.whose_go:
            return 0
        if self.last_column == 1:
            return 1
        if self.board[self.last_row][self.last_column - 2] != self.whose_go:
            return 1
        if self.last_column == 2:
            return 2
        if self.board[self.last_row][self.last_column - 3] != self.whose_go:
            return 2
        return 3

    def counters_right(self):
        if self.last_column == 6:
            return 0
        if self.board[self.last_row][self.last_column + 1] != self.whose_go:
            return 0
        if self.last_column == 5:
            return 1
        if self.board[self.last_row][self.last_column + 2] != self.whose_go:
            return 1
        if self.last_column == 4:
            return 2
        if self.board[self.last_row][self.last_column + 3] != self.whose_go:
            return 2
        return 3

    def draw_board(self):
        for row in self.board:
            for hole in row:
                if hole == 0:
                    print("\033[1;30m⚪", end=' ')
                elif hole == 1:
                    print("\033[1;31m🔴", end=' ')
                elif hole == 2:
                    print("\033[1;33m🔵", end=' ')
            print("\033[1;30m")
        print('1  2 3  4  5  6 7')
        print('')

    def add_counter(self, column, player):
        for row in range(len(self.board) - 1, 0, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = player
                self.last_column = column
                self.last_row = row
                break



game = Connect4()

while game.there_is_a_winner == False:
    game.play()



