class ConnectFour:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'
        self.winner = None

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 7)
        print('1 2 3 4 5 6 7')

    def drop_disc(self, column):
        for row in range(5, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                break
        else:
            print("Column is full. Try again.")
            return False
        return True

    def check_winner(self):
        # Check rows
        for row in range(6):
            for col in range(4):
                if (self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] ==
                        self.board[row][col + 3] != ' '):
                    self.winner = self.current_player
                    return True

        # Check columns
        for col in range(7):
            for row in range(3):
                if (self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] ==
                        self.board[row + 3][col] != ' '):
                    self.winner = self.current_player
                    return True

        # Check diagonal (top-left to bottom-right)
        for row in range(3):
            for col in range(4):
                if (self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] ==
                        self.board[row + 3][col + 3] != ' '):
                    self.winner = self.current_player
                    return True

        # Check diagonal (bottom-left to top-right)
        for row in range(3, 6):
            for col in range(4):
                if (self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] ==
                        self.board[row - 3][col + 3] != ' '):
                    self.winner = self.current_player
                    return True

        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while not self.winner:
            self.print_board()
            column = int(input(f"Player {self.current_player}, enter column (1-7): ")) - 1
            if 0 <= column <= 6:
                if self.drop_disc(column):
                    if self.check_winner():
                        self.print_board()
                        print(f"Player {self.current_player} wins!")
                        break
                    self.switch_player()
            else:
                print("Invalid column. Please enter a column between 1 and 7.")

        if not self.winner:
            self.print_board()
            print("It's a tie!")


# Example usage
game = ConnectFour()
game.play()
