class player:

    def make_turn(self, board):
        newRow = -1
        newCol = -1
        while int(newRow) < 0 or int(newRow) > 3:
            newRow = input("Select row: ")
        while int(newCol) < 0 or int(newCol) > 3:
            newCol = input("Select column: ")
        if board.is_empty([int(newRow) - 1, int(newCol) - 1]):
            board.make_turn('O', [int(newRow) - 1, int(newCol) - 1])
        else:
            print("already used")
            self.make_turn(board)
