from random import shuffle, randint
import typing

BoardType = typing.List[typing.List[typing.Union[None, int]]]    # type hint alias for board - a list of lists
                                                                 # with int or None as values
class Sudoku:
    """" A class that acts like a sudoku puzzle. """

    def __init__(self):  # noqa: ANN204
        self.counter = 1
        self.top_boxes = [_Box() for _ in range(3)]
        self.mid_boxes = [_Box() for _ in range(3)]
        self.bottom_boxes = [_Box() for _ in range(3)]

        self._set_box_locations()

        self.original = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                         [4, 5, 6, 7, 8, 9, 1, 2, 3],
                         [7, 8, 9, 1, 2, 3, 4, 5, 6],
                         [2, 3, 1, 5, 6, 4, 8, 9, 7],
                         [5, 6, 4, 8, 9, 7, 2, 3, 1],
                         [8, 9, 7, 2, 3, 1, 5, 6, 4],
                         [3, 1, 2, 6, 4, 5, 9, 7, 8],
                         [6, 4, 5, 9, 7, 8, 3, 1, 2],
                         [9, 7, 8, 3, 1, 2, 6, 4, 5]]

        self.generator()
        self.full_board = self.get_all_row_values()
        self.puzzle_maker()

    # Methods run at initialization.
    def _set_box_locations(self) -> None:  # Sets each of the box's position attribute.
        for i in self.top_boxes:
            i.box_pos = 'top'
        for i in self.mid_boxes:
            i.box_pos = 'mid'
        for i in self.bottom_boxes:
            i.box_pos = 'bottom'

    # Getter methods
    def get_column_values(self, index: int) -> list:  # returns column values in the form of
        box_index = index // 3  # a list. Indexing from 0-8 from
        element_index = index % 3  # left to right.
        column = []
        for i in range(9):
            if i % 3 == 0 and i > 1:
                box_index += 3
                element_index -= 9
            element = self[box_index][element_index]
            column.append(element.get_value())  # appends value of the element.
            element_index += 3
        return column

    def get_row_values(self, index: int) -> list:  # returns row values in the form of a list.
        box_index = (index // 3) * 3  # Indexing from 0-8 from top to bottom
        element_index = index % 3 * 3
        row = []
        for i in range(9):
            if i % 3 == 0 and i > 1:
                box_index += 1
                element_index -= 3
            element = self[box_index][element_index]
            row.append(element.get_value())
            element_index += 1
        return row

    def get_all_row_values(self) -> list:  # Return a list of all the rows.
        rows = []
        for i in range(9):
            row = self.get_row_values(i)
            rows.append(row)
        return rows

    # Puzzle-Generation methods
    def possible_cell_values(self, row: int, col: int) -> list:

        element_possibility = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for col_value in self.get_column_values(col):
            if col_value in element_possibility:  # Reoccurring in the same column
                element_possibility.remove(col_value)

        for row_value in self.get_row_values(row):
            if row_value in element_possibility:  # Reoccurring in the same row
                element_possibility.remove(row_value)

        for m in element_possibility:
            if m in [self[(row // 3) * 3 + col // 3][n].get_value() for n in range(9)]:
                element_possibility.remove(m)

        return element_possibility

    @staticmethod
    def check_complete(grid: list) -> bool:
        for i in grid:
            for x in i:
                if x == 0:
                    return False
        return True

    def generator(self) -> None:

        shuffled = []

        for i in range(3):
            rows = [self.original[i * 3], self.original[(i * 3) + 1], self.original[(i * 3) + 2]]

            shuffle(rows)
            shuffled.extend(rows)

        self.set_value_of_grid(shuffled, "row")
        shuffled = []

        for i in range(3):
            cols = [self.get_row_values(i * 3), self.get_row_values((i * 3) + 1), self.get_row_values((i * 3) + 2)]

            shuffle(cols)
            shuffled.extend(cols)

        self.set_value_of_grid(shuffled, "col")

    def set_value_of_grid(self, list_val: list, index_type: str) -> None:

        if index_type == "row":
            for box in range(9):
                for element in range(9):
                    self[box][element].set_value(list_val[(box // 3) * 3 + element // 3][(box % 3) * 3 + element % 3])
        elif index_type == "col":
            for box in range(9):
                for element in range(9):
                    self[box][element].set_value(list_val[(box % 3) * 3 + element % 3][(box // 3) * 3 + element // 3])

    def unique_sol_check(self, grid: list) -> bool:

        # Recursive method to check whether there is a unique solution for a number removed from grid
        for i in range(81):

            row = i // 9
            col = i % 9

            if grid[row][col] == 0:
                for value in range(10):
                    if value in self.possible_cell_values(row, col):
                        grid[row][col] = value
                        self.set_value_of_grid(grid, "row")
                        if self.check_complete(grid):
                            self.counter += 1
                            break
                        else:
                            if self.unique_sol_check(grid):
                                return True
                break
        grid[row][col] = 0
        self.set_value_of_grid(grid, "row")

    def puzzle_maker(self) -> None:

        # adds spaces to the finished board
        attempts = 5
        while attempts > 0:
            row = randint(0, 8)
            col = randint(0, 8)
            while self[row][col].get_value() == 0:
                row = randint(0, 8)
                col = randint(0, 8)
            backup = self[row][col].get_value()
            self[row][col].set_value(0)

            copy = self.get_all_row_values()

            self.counter = 0
            self.unique_sol_check(copy)

            if self.counter != 1:
                self[row][col].set_value(backup)
                attempts -= 1

    def check(self, user_input: list) -> bool or list:

        if user_input == self.full_board:
            return True
        else:
            return [[True if self.full_board[row][col] == user_input[row][col] else False for col in range(9)] for row in range(9)]

    # operator overloading methods.
    def __iter__(self):  # noqa: ANN204
        for i in self.top_boxes:  # x here is a box
            yield i  # iterates through the boxes in the same way as
        for i in self.mid_boxes:  # a matrix; i.e. left to right.
            yield i
        for i in self.bottom_boxes:
            yield i

    def __getitem__(self, index: int):  # noqa: ANN204
        count = 0  # returns box object at index 3
        for i in self:
            if count == index:
                return i
            count += 1

    def __eq__(self, b: "Sudoku") -> bool:  # functionality -> sudoku1 == sudoku2
        for box in range(9):  # compares all values of both sudokus.
            for element in range(9):
                if self[box][element].get_value() != b[box][element].get_value(): return False
        return True


class _Box:
    """ A class that acts like one of the nine 3x3 boxes in sudoku. """

    def __init__(self):  # noqa: ANN204
        self.top_row = [_Element() for _ in range(3)]
        self.mid_row = [_Element() for _ in range(3)]
        self.bottom_row = [_Element() for _ in range(3)]
        self.box_pos = None  # NOT USED

        self.set_element_box()
        self.set_element_row()

    # Methods run at initialization.
    def set_element_box(self) -> None:  # Sets the box attribute of the element.
        for element in self:
            element._box = self

    def set_element_row(self) -> None:  # Sets the row attribute of the element.
        for element in self.top_row:
            element._row = self.top_row
        for element in self.mid_row:
            element._row = self.mid_row
        for element in self.bottom_row:
            element._row = self.bottom_row

    # Operator overloading methods
    def __iter__(self):  # noqa: ANN204
        for element in self.top_row:  # Iterates in the same way as a matrix
            yield element  # i.e. from left to right.
        for element in self.mid_row:
            yield element
        for element in self.bottom_row:
            yield element

    def __getitem__(self, index: int):  # noqa: ANN204
        count = 0  # returns value of specified index.
        for element in self:  # indexing from 0-9; indexing is in the same way
            if count == index:  # as a matrix.
                return element
            count += 1

    def __setitem__(self, index: int, val: typing.Union[int, None]):  # noqa: ANN204
        count = 0  # assignment at a specific index.
        for element_place in range(9):
            if count == element_place:
                self[element_place].set_value(val)
            count += 1

    def __contains__(self, val: typing.Union[int, None]) -> bool:  # functionality -> val in box
        for element in self:  # returns True or False.
            if element.get_value() == val:
                return True
        return False


class _Element:
    """ A class that acts as the element(number) in one of the boxes of sudoku. """

    def __init__(self, value: typing.Optional[int]=None):   # noqa: ANN204
        self._box = None  # The box this element belongs to.   #NOT USED
        self._row = None  # The row this element belongs to.   #NOT USED
        self._value = value  # The value the element has.

    # getter methods.
    def get_box(self) -> typing.Any:  # To access the box this element belongs to.
        return self._box

    def get_value(self) -> typing.Any:  # To access the value this element has.
        return self._value

    def get_row(self) -> typing.Any:  # To access the row this element belongs to.
        return self._row

        # setter methods.

    def set_value(self, value: typing.Union[int, None]) -> None:  # To access the value this element will have.
        self._value = value
