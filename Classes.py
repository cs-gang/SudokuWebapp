'''
                            HOW TO USE THIS SUDOKU CLASS.
This consists of 3 classes :-
1. Sudoku class - The main sudoku class. This is the object you'll mostly be interacting with.
2. _Box class - The 3x3 box inside a sudoku. You'll be accessing it mostly through the sudoku object with indexing.
3. _Element class - The number inside a box. You'll be accessing it mostly through the box object that you access with the sudoku object.
Methods to use ->
1. sudokuobject.get_column(index) -> This returns the column in the form of a list of values according to the index you send in.
note: This contains directly the values of the elements
2. sudokuobject.get_row(index) -> This returns the row in the form of a list of values according to the index you send in.
note: This contains directly the values of the elements
3. _elementobject.get_value() -> This returns the actual value held by the object.
You'll mostly have to sue this when accessing it through indexing.
4. _elementobject.set_value() -> This allows you to change the value an element is holding.
Functionality of the objects ->
Sudoku -> 1. for i in sudoku:
          2. sudoku[0] - returns a box
_Box -> 1. for i in box:
        2. box[0] - returns an element
        3. box[0] = 2
        4. len(box)
Read through the documentation in the code too, it'll give you a better idea.
                                        END                                   
'''

import random
from random import shuffle


class Sudoku:
    """" A class that acts like a sudoku puzzle. """

    def __init__(self):
        self.top_boxes = [_Box() for i in range(3)]
        self.mid_boxes = [_Box() for i in range(3)]
        self.bottom_boxes = [_Box() for i in range(3)]

        self._set_box_locations()

    # Methods run at initialization.
    def _set_box_locations(self):  # Sets each of the box's position attribute.
        for i in self.top_boxes:
            i.box_pos = 'top'
        for i in self.mid_boxes:
            i.box_pos = 'mid'
        for i in self.bottom_boxes:
            i.box_pos = 'bottom'

    # Getter methods
    def get_column_values(self, index):  # returns column values in the form of
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

    def get_row_values(self, index):  # returns row values in the form of a list.
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

    def get_column(self, index):  # returns column in the form of
        box_index = index // 3  # a list. Indexing from 0-8 from
        element_index = index % 3  # left to right.
        column = []
        for i in range(9):
            if i % 3 == 0 and i > 1:
                box_index += 3
                element_index -= 9
            element = self[box_index][element_index]
            column.append(element)  # appends value of the element.
            element_index += 3
        return column

    def get_row(self, index):  # returns row in the form of a list.
        box_index = (index // 3) * 3  # Indexing from 0-8 from top to bottom
        element_index = index % 3 * 3
        row = []
        for i in range(9):
            if i % 3 == 0 and i > 1:
                box_index += 1
                element_index -= 3
            element = self[box_index][element_index]
            row.append(element)
            element_index += 1
        return row

    def get_all_columns(self):  # Returns a list of all the columns.
        columns = []
        for i in range(9):
            columns.append(self.get_column(i))
        return columns

    def get_all_rows(self):  # Return a list of all the rows.
        rows = []
        for i in range(9):
            row = self.get_row(i)
            rows.append(row)
        return rows

    def get_indices(self, val):  # returns index of element in all boxes.
        box_index = 0  # the indexes are in the form of a tuple
        indices = []  # first element of tuple is the box index
        for box in self:  # second element of tuple is the element
            if val in box:  # index.
                indices.append((box_index, box.get_index(val)))
            box_index += 1
        return indices

    def possible_cell_values(self, box_no, element_no):

        x_coord = (box_no % 3) * 3 + element_no % 3  # Conversion from [box][element]
        y_coord = (box_no // 3) * 3 + element_no // 3

        element_possibility = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for col_value in self.get_column_values(x_coord):  # To remove the possibility of numbers
            if col_value in element_possibility:  # Reoccurring in the same column
                element_possibility.remove(col_value)

        for row_value in self.get_row_values(y_coord):  # To remove the possibility of numbers
            if row_value in element_possibility:  # Reoccurring in the same row
                element_possibility.remove(row_value)

        for m in element_possibility:
            if m in [self[box_no][n].get_value() for n in range(9)]:
                element_possibility.remove(m)

        return element_possibility

    def generator(self):

        if not Sudoku[0][0]:
            self.initial_puzzle()

        shuffled_rows = []

        for i in range(3):
            row1 = self.get_row_values(i * 3)
            row2 = self.get_row_values((i * 3) + 1)
            row3 = self.get_row_values((i * 3) + 2)
            rows = [row1, row2, row3]
            shuffle(rows)
            for i in rows:
                shuffled_rows.append(i)

        self.initial_puzzle(shuffled_rows)

    def initial_puzzle(self, inp=None):

        if inp is None:
            list_val = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [4, 5, 6, 7, 8, 9, 1, 2, 3],
                        [7, 8, 9, 1, 2, 3, 4, 5, 6],
                        [2, 3, 1, 5, 6, 4, 8, 9, 7],
                        [5, 6, 4, 8, 9, 7, 2, 3, 1],
                        [8, 9, 7, 2, 3, 1, 5, 6, 4],
                        [3, 1, 2, 6, 4, 5, 9, 7, 8],
                        [6, 4, 5, 9, 7, 8, 3, 1, 2],
                        [9, 7, 8, 3, 1, 2, 6, 4, 5]]
        else:
            list_val = inp

        for box in range(9):
            for element in range(9):
                self[box][element].set_value(list_val[(box // 3) * 3 + element // 3][(box % 3) * 3 + element % 3])

    def print_board(self):
        for w in range(0, 3):  # This is for temporary display
            co1 = 3 * w  # factor to print rows of boxes
            print("\n+=======================+", end="")
            for z in range(0, 3):
                co2 = 3 * z  # factor to print rows of values
                print("")
                for l in range(0, 3):  # To print first 3 boxes
                    for m in range(0, 3):  # To print first 3 element of a box, i.e., completing a row
                        if m == 0 and l == 0:
                            print("| ", end="")
                        if self[l + co1][m + co2].get_value() != None:
                            print(f"{self[l + co1][m + co2].get_value()} ", end="")
                        else:
                            print("  ", end="")
                        if m == 2:
                            print("| ", end="")
        print("\n+=======================+")

    # operator overloading methods.
    def __iter__(self):  # functionality -> for x in sudoku:
        for i in self.top_boxes:  # x here is a box
            yield i  # iterates through the boxes in the same way as
        for i in self.mid_boxes:  # a matrix; i.e. left to right.
            yield i
        for i in self.bottom_boxes:
            yield i

    def __getitem__(self, index):  # functionality -> returns value of sudoku[3]
        count = 0  # returns box object at index 3
        for i in self:
            if count == index:
                return i
            count += 1

    def __eq__(self, b):  # functionality -> sudoku1 == sudoku2
        for box in range(9):  # compares all values of both sudokus.
            for element in range(9):
                if self[box][element].get_value() != b[box][element].get_value(): return False
        return True


class _Box:
    """ A class that acts like one of the nine 3x3 boxes in sudoku. """

    def __init__(self):
        self.top_row = [_Element() for i in range(3)]
        self.mid_row = [_Element() for i in range(3)]
        self.bottom_row = [_Element() for i in range(3)]
        self.box_pos = None  # NOT USED

        self.set_element_box()
        self.set_element_row()

    # Methods run at initialization.
    def set_element_box(self):  # Sets the box attribute of the element.
        for element in self:
            element._box = self

    def set_element_row(self):  # Sets the row attribute of the element.
        for element in self.top_row:
            element._row = self.top_row
        for element in self.mid_row:
            element._row = self.mid_row
        for element in self.bottom_row:
            element._row = self.bottom_row

            # General methods

    def get_index(self, val):  # Returns the index of an element.
        count = 0
        for i in self:
            if i.get_value() == val:
                return count
            count += 1

    # Operator overloading methods
    def __iter__(self):  # functionality -> for x in box:
        for element in self.top_row:  # Iterates in the same way as a matrix
            yield element  # i.e. from left to right.
        for element in self.mid_row:
            yield element
        for element in self.bottom_row:
            yield element

    def __getitem__(self, index):  # functionality -> getting value of box[3]
        count = 0  # returns value of specified index.
        for element in self:  # indexing from 0-9; indexing is in the same way
            if count == index:  # as a matrix.
                return element
            count += 1

    def __setitem__(self, index, val):  # functionality -> assignment box[2]=3
        count = 0  # assignment at a specific index.
        for element_place in range(9):
            if count == element_place:
                self[element_place].set_value(val)
            count += 1

    def __contains__(self, val):  # functionality -> val in box
        for element in self:  # returns True or False.
            if element.get_value() == val:
                return True
        return False


class _Element:
    ''' A class that acts as the element(number) in one of the boxes of sudoku. '''

    def __init__(self, value=None):
        self._box = None  # The box this element belongs to.   #NOT USED
        self._row = None  # The row this element belongs to.   #NOT USED
        self._value = value  # The value the element has.

    # getter methods.
    def get_box(self):  # To access the box this element belongs to.
        return self._box

    def get_value(self):  # To access the value this element has.
        return self._value

    def get_row(self):  # To access the row this element belongs to.
        return self._row

        # setter methods.

    def set_value(self, value):  # To access the value this element will have.
        self._value = value


"""
=============================================================================

                                Testing

=============================================================================
"""

'''                      Initializing the sudoku generator!                        '''

Test = Sudoku()

Test.initial_puzzle()

Test.print_board()

Test.generator()

Test.print_board()

"""
l = []
for h in range(0, 9):
    l.append(list(map(_Element.get_value, Test.get_row(h))))
print(l)

l1 = [list(map(_Element.get_value, i)) for i in Test.get_all_rows()]
print(l1)
"""