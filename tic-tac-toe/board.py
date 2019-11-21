class board:
    array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def print_it(self):
        for row in range(3):
            print(self.array[row])

    def make_turn(self, sign, position):
        self.array[position[0]][position[1]] = sign

    def is_empty(self, position):
        return self.array[position[0]][position[1]] == ' '

    def is_player(self, position):
        return self.array[position[0]][position[1]] == 'O'

    def is_cpu(self, position):
        return self.array[position[0]][position[1]] == 'X'

    def is_finished(self):
        for row in range(3):
            amount = 0
            for col in range(3):
                if self.is_player([row, col]):
                    amount = amount + 1
                elif self.is_cpu([row, col]):
                    amount = amount - 1
            if amount == 3:
                print('YOU WON')
                return 1
            if amount == -3:
                print('YOU LOST')
                return 1

        for row in range(3):
            amount = 0
            for col in range(3):
                if self.is_player([col, row]):
                    amount = amount + 1
                elif self.is_cpu([col, row]):
                    amount = amount - 1
            if amount == 3:
                print('YOU WON')
                return 1
            if amount == -3:
                print('YOU LOST')
                return 1

        amount = 0
        for pos in range(3):
            if self.is_player([pos, pos]):
                amount = amount + 1
            if self.is_cpu([pos, pos]):
                amount = amount - 1
        if amount == 3:
            print('YOU WON')
            return 1
        if amount == -3:
            print('YOU LOST')
            return 1

        if self.is_player([0, 2]) and self.is_player([2, 0]) and self.is_player([1, 1]):
            print('YOU WON')
            return 1

        if self.is_cpu([0, 2]) and self.is_cpu([2, 0]) and self.is_cpu([1, 1]):
            print('YOU LOST')
            return 1

        for row in range(3):
            for col in range(3):
                if self.is_empty([row, col]):
                    return 0

        print('NO WINNER')
        return 1

