
class Board:
    board = []

    def __init__(self):
        self.board = [' ', " ", " ", " ", ' ', " ", " ", " ", ' ']

    def modify(self, place_number, shape):
        self.board[place_number] = shape

    def draw_board(self):
        print()
        print(self.board[0], "|", self.board[1], "|", self.board[2])
        print("--|---|--")
        print(self.board[3], "|", self.board[4], "|", self.board[5])
        print("--|---|--")
        print(self.board[6], "|", self.board[7], "|", self.board[8])

    def win_checker(self, player_shape0, computer_shape0):
        count = 0
        for x in range(0, 3):
            if self.board[x + 6] != " " and self.board[x] == self.board[x + 3] and self.board[x] == self.board[x + 6]:
                if self.board[x] == player_shape0:
                    return -1
                return 1
        if (self.board[2] == self.board[4] and self.board[4] == self.board[6]) or (
                self.board[0] == self.board[4] and self.board[4] == self.board[8]):
            if self.board[4] == player_shape0:
                return -1
            if self.board[4] == computer_shape0:
                return 1
        for x in range(0, 7, 3):
            if self.board[x + 2] != " " and self.board[x] == self.board[x + 1] and self.board[x] == self.board[x + 2]:
                if self.board[x] == player_shape0:
                    return -1
                return 1
        for i in range(0, 9):
            if self.board[i] != " ":
                count = count + 1
        if count == 9:
            return 0
