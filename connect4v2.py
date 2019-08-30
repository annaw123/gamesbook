class Connect4:

    def __init__(self):
        print('hello')
        self.get_player_names()
        self.whose_go = 0
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
        print('Where would you like to go,', self.players[self.whose_go])
        column = int(input()) - 1
        self.add_counter(column, self.whose_go + 1)
        if self.player_has_won():
            print('Hooray')
            self.there_is_a_winner = True
        else:
            self.whose_go = 1 - self.whose_go

    def player_has_won(self):
        False

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
        for row_index in range(len(self.board) - 1, 0, -1):
            if self.board[row_index][column] == 0:
                self.board[row_index][column] = player
                break



game = Connect4()

while game.there_is_a_winner == False:
    game.play()



