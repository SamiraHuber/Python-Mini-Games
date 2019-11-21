class cpu:

    def add_third_in_row(self, board):
        for row in range(3):
            amount = 0
            for col in range(3):
                if board.is_cpu([row, col]):
                    amount = amount + 1
                elif board.is_player([row, col]):
                    amount = amount - 1
            if amount is 2:
                for col in range(3):
                    if board.is_empty([row, col]):
                        board.make_turn('X', [row, col])
                        return 1
        return 0

    def add_third_in_column(self, board):
        for row in range(3):
            amount = 0
            for col in range(3):
                if board.is_cpu([col, row]):
                    amount = amount + 1
                elif board.is_player([col, row]):
                    amount = amount - 1
            if amount is 2:
                for col in range(3):
                    if board.is_empty([col, row]):
                        board.make_turn('X', [col, row])
                        return 1
        return 0

    def add_third_diagonal(self, board):
        amount = 0
        for pos in range(3):
            if board.is_cpu([pos, pos]):
                amount = amount + 1
            if board.is_player([pos, pos]):
                amount = amount - 1
        if amount == 2:
            for pos in range(3):
                if board.is_empty([pos, pos]):
                    board.make_turn('X', [pos, pos])
                    return 1

        if board.is_cpu([0, 2]) or board.is_cpu([2, 0]):
            if board.is_cpu([1, 1]) or (board.is_cpu([0, 2]) and board.is_cpu([2, 0])):
                if board.is_empty([0, 2]):
                    board.make_turn('X', [0, 2])
                    return 1
                elif board.is_empty([1, 1]):
                    board.make_turn('X', [1, 1])
                    return 1
                elif board.is_empty([2, 0]):
                    board.make_turn('X', [2, 0])
                    return 1
        return 0


    def block_third_in_row(self, board):
        for row in range(3):
            amount = 0
            for col in range(3):
                if board.is_player([row, col]):
                    amount = amount + 1
                elif board.is_cpu([row, col]):
                    amount = amount - 1
            if amount is 2:
                for col in range(3):
                    if board.is_empty([row, col]):
                        board.make_turn('X', [row, col])
                        return 1
        return 0


    def block_third_in_column(self, board):
        for row in range(3):
            amount = 0
            for col in range(3):
                if board.is_player([col, row]):
                    amount = amount + 1
                elif board.is_cpu([col, row]):
                    amount = amount - 1
            if amount is 2:
                for col in range(3):
                    if board.is_empty([col, row]):
                        board.make_turn('X', [col, row])
                        return 1
        return 0


    def block_third_diagonal(self, board):
        amount = 0
        for pos in range(3):
            if board.is_player([pos, pos]):
                amount = amount + 1
            if board.is_cpu([pos, pos]):
                amount = amount - 1
        if amount == 2:
            for pos in range(3):
                if board.is_empty([pos, pos]):
                    board.make_turn('X', [pos, pos])
                    return 1

        if board.is_player([0, 2]) or board.is_player([2, 0]):
            if board.is_player([1, 1]) or (board.is_player([0, 2]) and board.is_player([2, 0])):
                if board.is_empty([0, 2]):
                    board.make_turn('X', [0, 2])
                    return 1
                elif board.is_empty([1, 1]):
                    board.make_turn('X', [1, 1])
                    return 1
                elif board.is_empty([2, 0]):
                    board.make_turn('X', [2, 0])
                    return 1
        return 0


    def try_to_win(self, board):
        success = self.add_third_in_row(board)
        if success == 1:
            return success
        success = self.add_third_in_column(board)
        if success == 1:
            return success
        success = self.add_third_diagonal(board)
        return success


    def try_to_block(self, board):
        success = self.block_third_in_row(board)
        if success == 1:
            return success
        success = self.block_third_in_column(board)
        if success == 1:
            return success
        success = self.block_third_diagonal(board)
        return success


    def try_to_fork(self, board):
        array = []
        for row in range(3):
            amount = 0
            empty_fiels = []
            for column in range(3):
                if board.is_empty([row, column]):
                    amount = amount + 1
                    empty_fiels.append([row, column])
                if board.is_player([row, column]):
                    amount = amount - 1
            if amount == 2:
                for val in range(len(empty_fiels)):
                    array.append(empty_fiels[val])

        for row in range(3):
            amount = 0
            empty_fiels = []
            for column in range(3):
                if board.is_empty([column, row]):
                    amount = amount + 1
                    empty_fiels.append([column, row])
                if board.is_player([column, row]):
                    amount = amount - 1
            if amount == 2:
                for val in range(len(empty_fiels)):
                    array.append(empty_fiels[val])

        amount = 0
        empty_fiels = []
        for pos in range(3):
            if board.is_empty([pos, pos]):
                amount = amount + 1
                empty_fiels.append([pos, pos])
            elif board.is_player([pos, pos]):
                amount = amount - 1
        if amount == 2:
            for val in range(len(empty_fiels)):
                array.append(empty_fiels[val])

        empty_fiels = []

        if board.is_empty([0, 2]) or board.is_empty([2, 0]):
            if board.is_empty([1, 1]) or (board.is_empty([0, 2]) and board.is_empty([2, 0])):
                if board.is_empty([0, 2]):
                    empty_fiels.append([0, 2])
                elif board.is_empty([1, 1]):
                    empty_fiels.append([1, 1])
                elif board.is_empty([2, 0]):
                    empty_fiels.append([2, 0])

        for val in range(len(empty_fiels)):
            array.append(empty_fiels[val])

        for arr in range(len(array)):
            for compare_arr in range(arr + 1, len(array) - 1):
                if array[arr] == array[compare_arr]:
                    board.make_turn('X', array[arr])
                    return 1

        return 0

    def block_fork(self, board):
        array = []
        for row in range(3):
            amount = 0
            empty_fiels = []
            for column in range(3):
                if board.is_empty([row, column]):
                    amount = amount + 1
                    empty_fiels.append([row, column])
                if board.is_cpu([row, column]):
                    amount = amount - 1
            if amount == 2:
                for val in range(len(empty_fiels)):
                    array.append(empty_fiels[val])

        for row in range(3):
            amount = 0
            empty_fiels = []
            for column in range(3):
                if board.is_empty([column, row]):
                    amount = amount + 1
                    empty_fiels.append([column, row])
                if board.is_cpu([column, row]):
                    amount = amount - 1
            if amount == 2:
                for val in range(len(empty_fiels)):
                    array.append(empty_fiels[val])

        amount = 0
        empty_fiels = []
        for pos in range(3):
            if board.is_empty([pos, pos]):
                amount = amount + 1
                empty_fiels.append([pos, pos])
            elif board.is_cpu([pos, pos]):
                amount = amount - 1
        if amount == 2:
            for val in range(len(empty_fiels)):
                array.append(empty_fiels[val])

        empty_fiels = []

        if board.is_empty([0, 2]) or board.is_empty([2, 0]):
            if board.is_empty([1, 1]) or (board.is_empty([0, 2]) and board.is_empty([2, 0])):
                if board.is_empty([0, 2]):
                    empty_fiels.append([0, 2])
                elif board.is_empty([1, 1]):
                    empty_fiels.append([1, 1])
                elif board.is_empty([2, 0]):
                    empty_fiels.append([2, 0])

        for val in range(len(empty_fiels)):
            array.append(empty_fiels[val])

        for arr in range(len(array)):
            for compare_arr in range(arr + 1, len(array) - 1):
                if array[arr] == array[compare_arr]:
                    board.make_turn('X', array[arr])
                    return 1

        return 0

    def play_center(self, board):
        if board.is_empty([1, 1]):
            board.make_turn('X', [1, 1])
            return 1
        return 0

    def opposite_corner(self, board):
        if board.is_player([0, 0]) and board.is_empty([2, 2]):
            board.make_turn('X', [2, 2])
            return 1
        elif board.is_player([2, 2]) and board.is_empty([0, 0]):
            board.make_turn('X', [0, 0])
            return 1
        elif board.is_player([0, 2]) and board.is_empty([2, 0]):
            board.make_turn('X', [2, 0])
            return 1
        elif board.is_player([2, 0]) and board.is_empty([0, 2]):
            board.make_turn('X', [0, 2])
            return 1
        return 0

    def any_corner(self, board):
        if board.is_empty([2, 2]):
            board.make_turn('X', [2, 2])
            return 1
        elif board.is_empty([0, 0]):
            board.make_turn('X', [0, 0])
            return 1
        elif board.is_empty([2, 0]):
            board.make_turn('X', [2, 0])
            return 1
        elif board.is_empty([0, 2]):
            board.make_turn('X', [0, 2])
            return 1
        return 0

    def any_side(self, board):
        if board.is_empty([0, 1]):
            board.make_turn('X', [0, 1])
            return 1
        elif board.is_empty([1, 2]):
            board.make_turn('X', [1, 2])
            return 1
        elif board.is_empty([2, 1]):
            board.make_turn('X', [2, 1])
            return 1
        elif board.is_empty([1, 0]):
            board.make_turn('X', [1, 0])
            return 1
        return 0

    def make_turn(self, board):
        # WIN
        success = self.try_to_win(board)
        if success == 1:
            return

        # BLOCK
        success = self.try_to_block(board)
        if success == 1:
            return

        # FORK
        success = self.try_to_fork(board)
        if success == 1:
            return

        # BLOCK FORK
        success = self.block_fork(board)
        if success == 1:
            return

        # CENTER
        success = self.play_center(board)
        if success == 1:
            return

        # OPPOSITE CORNER
        success = self.opposite_corner(board)
        if success == 1:
            return

        # EMPTY CORNER
        success = self.any_corner(board)
        if success == 1:
            return

        # EMPTY SIDE
        success = self.any_side(board)
        if success == 1:
            return

        print("error")
