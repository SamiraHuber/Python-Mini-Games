import copy

class solver:
    array = [
        [0, 0, 0, 7, 0, 5, 0, 0, 4],
        [0, 1, 0, 0, 0, 4, 8, 0, 0],
        [4, 6, 0, 8, 3, 2, 0, 0, 0],
        # ----------------------------
        [0, 0, 6, 9, 0, 0, 1, 3, 2],
        [0, 0, 8, 0, 0, 0, 5, 0, 0],
        [5, 2, 3, 0, 0, 1, 7, 0, 0],
        # ----------------------------
        [0, 0, 0, 1, 8, 3, 0, 2, 7],
        [0, 0, 2, 5, 0, 0, 0, 8, 0],
        [3, 0, 0, 2, 0, 6, 0, 0, 0]
    ]
    filledArray = []
    counter = 0

    def __init__(self):
        self.filledArray = copy.deepcopy(self.array)

    def print_board(self):
        for line in range(len(self.filledArray)):
            print(self.filledArray[line])

    def find_solution(self):
        field = self.find_next_empty_field(0, -1)
        self.calculate_solution(field[0], field[1])
        print(self.counter)

    def calculate_solution(self, row, column):
        is_success = self.find_value(row, column)
        if is_success == 1:
            field = self.find_next_empty_field(row, column)
            if field != None:
                self.calculate_solution(field[0], field[1])
            else:
                return
        else:
            field = self.find_last_empty_field(row, column)
            # if recursion is called more than 487 times, there is a error message
            if field != None and self.filledArray[row][column] < 9 and self.counter < 486:
                self.counter = self.counter + 1
                self.calculate_solution(field[0], field[1])

    def find_value(self, row, column):
        old_val = self.filledArray[row][column];
        self.filledArray[row][column] = 0
        for val in range(old_val + 1, 10):
            if self.check_line(row, val) == 0 and self.check_column(column, val) == 0 and self.check_box(self.get_box(row, column), val) == 0:
                self.filledArray[row][column] = val
                return 1
        return 0

    def find_next_empty_field(self, lastRow, lastColumn):
        for column in range(lastColumn + 1, len(self.filledArray[lastRow])):
            if self.filledArray[lastRow][column] == 0:
                return [lastRow, column]

        for row in range(lastRow + 1, len(self.filledArray)):
            for column in range(0, len(self.filledArray[row])):
                if self.array[row][column] == 0:
                    return [row, column]

    def find_last_empty_field(self, lastRow, lastColumn):
        for column in range(lastColumn - 1, -1, -1):
            if self.array[lastRow][column] == 0:
                return [lastRow, column]

        for row in range(lastRow - 1, -1, -1):
            for column in range(8, -1, -1):
                if self.array[row][column] == 0:
                    return [row, column]

    def check_line(self, row, number):
        for column in range(len(self.filledArray[row])):
            if self.filledArray[row][column] == number:
                return 1
        return 0

    def check_column(self, column, number):
        for row in range(len(self.filledArray)):
            if self.filledArray[row][column] == number:
                return 1
        return 0

    def get_box(self, row, column):
        if row < 3:
            if column < 3:
                return 1
            elif column < 6:
                return 2
            return 3
        elif row < 6:
            if column < 3:
                return 4
            elif column < 6:
                return 5
            return 6
        else:
            if column < 3:
                return 7
            elif column < 6:
                return 8
            return 9

    def check_box(self, box, number):
        startRow = 0
        startColumn = 0
        if box == 2:
            startColumn = 3
        elif box == 3:
            startColumn = 6
        elif box == 4:
            startRow = 3
            startColumn = 0
        elif box == 5:
            startRow = 3
            startColumn = 3
        elif box == 6:
            startRow = 3
            startColumn = 6
        elif box == 7:
            startRow = 6
            startColumn = 0
        elif box == 8:
            startRow = 6
            startColumn = 3
        elif box == 9:
            startRow = 6
            startColumn = 6

        for row in range(startRow, startRow + 3):
            for column in range(startColumn, startColumn + 3):
                if self.filledArray[row][column] == number:
                    return 1
        return 0