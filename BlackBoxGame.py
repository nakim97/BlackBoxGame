# Name: Na Kim
# Date: 08/3/2020
# Description: This written program represents the game, BlackBox that takes place on a 10x10 grid.

class BlackBoxGame:
    """ Represents the game,BlackBox, with atoms and ray entrance/exit, that takes place on a 10 x 10 grid"""

    def __init__(self, atom_location):
        """Initializes the grid for the game,BlackBox, that takes a list of (row,column) tuples as a parameter to mark
        the location of atoms placed on the board as well as other data members"""
        self._atom_location = atom_location  # atom location coordinates
        self._score = 25  # score total starts with 25 points
        self._atom_count = 0  # counts atoms guessed
        self._guess = [] # stores guesses in list

    def hit_ray(self, row, column):
        """Returns whether the ray shot hits an atom on the board (known as a HIT), then returns """
        # If the chosen row and column is a corner square, ray cannot be shot, thus Return False
        if (row == 0 and column == 9) or (row == 0 and column == 0) or (row == 9 and column == 0) or (
                row == 9 and column == 9):
            return False
        # If the chosen row and column is on border square, shoot ray is possible. If not on border, False
        if (row == 0 and 0 <= column <= 9) or (column == 0 and 0 <= row <= 9) or (row == 9 and 0 <= column <= 9) or (
                0 <= row <= 9 and column == 9):
            # Use list comprehension to create list of row elements of atoms placed on board
            check_row = [i[0] for i in self._atom_location]
            # Use list comprehension to create list of column elements of atoms placed on board
            check_column = [i[1] for i in self._atom_location]
            # Use Set function to see if certain value exists in list of elements of atom row or column
            rows = set(check_row)
            columns = set(check_column)
            # If ray shot's row/column equals atom placed row/column, there is a Hit, return True
            if (0 <= row <= 9 and column == 0):  # direction from left to right side of board
                if row in rows:
                    self._score -= 1  # if there is a hit, subtract 1 point
                    return None
            if (0 <= row <= 9 and column == 9):  # direction from right to left side of board
                if row in rows:
                    self._score -= 1
                    return None
            if (row == 0 and 0 <= column <= 9):  # direction from top to bottom of board
                if column in columns:
                    self._score -= 1
                    return None
            if (row == 9 and 0 <= column <= 9):  # direction from bottom to top of board
                if column in columns:
                    self._score -= 1
                    return None
        else:
            return False  # Return False if chosen row/column is NOT on border square


    def miss_ray(self, row, column):
        """Returns whether the ray shot misses, if True, returns the exit position of ray"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        # If the ray shot's row or column does not have atom placed, the ray exit coordinate returned based on
        # ray direction/board position.
        if not(self.reflection_ray(row, column) or self.deflect_west_left(row, column) or
        self.deflect_west_right(row, column) or self.deflect_east_left(row, column) or
        self.deflect_east_right(row, column) or self.deflect_top_left(row, column) or
        self.deflect_top_right(row, column) or self.deflect_bottom_left(row, column) or
        self.deflect_bottom_right(row, column) or self.double_deflection_west(row, column) or
        self.double_deflection_east(row, column) or self.double_deflection_top(row, column) or
        self.double_deflection_bottom(row, column) or self.helper_double(row, column) or
        self.helper_deflection(row, column) or self.detour_west(row, column) or
        self.detour_east(row, column) or self.detour_bottom(row, column) or
        self.detour_top(row, column) or self.detour_helper(row,column)):
            if (0 <= row <= 9 and column == 0):  # direction from left to right of board
                if row not in rows:
                    return (row, column + 9)
            if (0 <= row <= 9 and column == 9):  # direction from right to left of board
                if row not in rows:
                    return (row, column - 9)
            if (row == 0 and 1 <= column <= 9):  # direction from top to bottom of board
                if column not in columns:
                    return (row + 9, column)
            if (row == 9 and 1 <= column <= 9):  # direction from bottom to top of board
                if column not in columns:
                    return (row - 9, column)

    def reflection_ray(self, row, column):
        """Returns whether the ray shot is reflected by atoms"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        # checking to see if there is an atom to left of ray (atom must be on edge)
        if (row - 1) in rows and (column + 1) in columns:  # from left to right side of board
            return (row, column)
        if (row + 1) in rows and (column - 1) in columns:  # from right to left side of board
            return (row, column)
        if (row + 1) in rows and (column + 1) in columns:  # from top to bottom side of board
            return (row, column)
        if (row - 1) in rows and (column - 1) in columns:  # from bottom to top side of board
            return (row, column)
        # checking to see if there is an atom to right of ray (atom must be on edge)
        if (row + 1) in rows and (column + 1) in columns:  # from left to right side of board
            return (row, column)
        if (row - 1) in rows and (column - 1) in columns:  # from right to left side of board
            return (row, column)
        if (row + 1) in rows and (column - 1) in columns:  # from top to bottom side of board
            return (row, column)
        if (row - 1) in rows and (column + 1) in columns:  # from bottom to top side of board
            return (row, column)





    def deflect_west_left(self, row, column):
        """Returns interaction if ray is deflected by an atom to the left of ray from left to right side of board"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        if (0 <= row <= 9) and (column == 0):
            if (row - 1) in rows and (column + 2) in columns:
                return (9, column + 1)
            if (row - 1) in rows and (column + 3) in columns:
                return (9, column + 2)
            if (row - 1) in rows and (column + 4) in columns:
                return (9, column + 3)
            if (row - 1) in rows and (column + 5) in columns:
                return (9, column + 4)
            if (row - 1) in rows and (column + 6) in columns:
                return (9, column + 5)
            if (row - 1) in rows and (column + 7) in columns:
                return (9, column + 6)
            if (row - 1) in rows and (column + 8) in columns:
                return (9, column + 7)

    def deflect_west_right(self, row, column):
        """Returns interaction if ray is deflected by an atom to the right from left to right side of board"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        if (0 <= row <= 9) and (column == 0):
            if (row + 1) in rows and (column + 2) in columns:
                return (0, column + 1)
            if (row + 1) in rows and (column + 3) in columns:
                return (0, column + 2)
            if (row + 1) in rows and (column + 4) in columns:
                return (0, column + 3)
            if (row + 1) in rows and (column + 5) in columns:
                return (0, column + 4)
            if (row + 1) in rows and (column + 6) in columns:
                return (0, column + 5)
            if (row + 1) in rows and (column + 7) in columns:
                return (0, column + 6)
            if (row + 1) in rows and (column + 8) in columns:
                return (0, column + 7)

    def deflect_east_left(self, row, column):
        """Returns interaction if ray is deflected by an atom to the left from right to left side of board"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        if (0 <= row <= 9) and (column == 9):
            if (row + 1) in rows and (column - 2) in columns:
                return (0, column - 1)
            if (row + 1) in rows and (column - 3) in columns:
                return (0, column - 2)
            if (row + 1) in rows and (column - 4) in columns:
                return (0, column - 3)
            if (row + 1) in rows and (column - 5) in columns:
                return (0, column - 4)
            if (row + 1) in rows and (column - 6) in columns:
                return (0, column - 5)
            if (row + 1) in rows and (column - 7) in columns:
                return (0, column - 6)
            if (row + 1) in rows and (column - 8) in columns:
                return (0, column - 7)

    def deflect_east_right(self, row, column):
        """Returns interaction if ray is deflected by an atom to the right from the right to left side of board"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        if (0 <= row <= 9) and (column == 9):
            if (row - 1) in rows and (column - 2) in columns:
                return (9, column - 1)
            if (row - 1) in rows and (column - 3) in columns:
                return (9, column - 2)
            if (row - 1) in rows and (column - 4) in columns:
                return (9, column - 3)
            if (row - 1) in rows and (column - 5) in columns:
                return (9, column - 4)
            if (row - 1) in rows and (column - 6) in columns:
                return (9, column - 5)
            if (row - 1) in rows and (column - 7) in columns:
                return (9, column - 6)
            if (row - 1) in rows and (column - 8) in columns:
                return (9, column - 7)

    def deflect_top_left(self, row, column):
        """Returns interaction if ray is deflected by an atom to the left from top to bottom side of board"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        if (row == 0) and (0 <= column <= 9):
            if (column + 1) in columns and (row + 2) in rows:
                return (row + 1, 0)
            if (column + 1) in columns and (row + 3) in rows:
                return (row + 2, 0)
            if (column + 1) in columns and (row + 4) in rows:
                return (row + 3, 0)
            if (column + 1) in columns and (row + 5) in rows:
                return (row + 4, 0)
            if (column + 1) in columns and (row + 6) in rows:
                return (row + 5, 0)
            if (column + 1) in columns and (row + 7) in rows:
                return (row + 6, 0)
            if (column + 1) in columns and (row + 8) in rows:
                return (row + 7, 0)


    def deflect_top_right(self, row, column):
        """Returns interaction if ray is deflected by an atom to the right from top to bottom side of board"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        if (row == 0) and (0 <= column <= 9):
            if (column - 1) in columns and (row + 2) in rows:
                return (row + 1, 9)
            if (column - 1) in columns and (row + 3) in rows:
                return (row + 2, 9)
            if (column - 1) in columns and (row + 4) in rows:
                return (row + 3, 9)
            if (column - 1) in columns and (row + 5) in rows:
                return (row + 4, 9)
            if (column - 1) in columns and (row + 6) in rows:
                return (row + 5, 9)
            if (column - 1) in columns and (row + 7) in rows:
                return (row + 6, 9)
            if (column - 1) in columns and (row + 8) in rows:
                return (row + 7, 9)

    def deflect_bottom_left(self, row, column):
        """Returns interaction if ray is deflected by an atom to the left from bottom to top side of board"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        if (row == 9) and (0 <= column <= 9):
            if (row - 2) in rows and (column - 1) in columns:
                return (row - 1, 9)
            if (row - 3) in rows and (column - 1) in columns:
                return (row - 2, 9)
            if (row - 4) in rows and (column - 1) in columns:
                return (row - 3, 9)
            if (row - 5) in rows and (column - 1) in columns:
                return (row - 4, 9)
            if (row - 6) in rows and (column - 1) in columns:
                return (row - 5, 9)
            if (row - 7) in rows and (column - 1) in columns:
                return (row - 6, 9)
            if (row - 8) in rows and (column - 1) in columns:
                return (row - 7, 9)

    def deflect_bottom_right(self, row, column):
        """Returns interaction if ray is deflected by an atom to the right from bottom to top side of board"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        if (row == 9) and (0 <= column <= 9):
            if (row - 2) in rows and (column + 1) in columns:
                return (row - 1, 0)
            if (row - 3) in rows and (column + 1) in columns:
                return (row - 2, 0)
            if (row - 4) in rows and (column + 1) in columns:
                return (row - 3, 0)
            if (row - 5) in rows and (column + 1) in columns:
                return (row - 4, 0)
            if (row - 6) in rows and (column + 1) in columns:
                return (row - 5, 0)
            if (row - 7) in rows and (column + 1) in columns:
                return (row - 6, 0)
            if (row - 8) in rows and (column + 1) in columns:
                return (row - 7, 0)

    def double_deflection_west(self, row, column):
        """Returns interaction if there is a double deflection that occurs on left side of board"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        west_left_1 = (row-1 in rows and column+2 in columns)
        west_left_2 = (row-1 in rows and column+3 in columns)
        west_left_3 =(row-1 in rows and column+4 in columns)
        west_left_4 =(row-1 in rows and column+5 in columns)
        west_left_5 = (row-1 in rows and column+6 in columns)
        west_left_6 =(row-1 in rows and column+7 in columns)
        west_left_7 =(row-1 in rows and column+8 in columns)
        west_right_1 = (row + 1 in rows and column + 2 in columns)
        west_right_2 = (row + 1 in rows and column + 3 in columns)
        west_right_3 =(row + 1 in rows and column + 4 in columns)
        west_right_4 = (row + 1 in rows and column + 5 in columns)
        west_right_5 =(row + 1 in rows and column + 6 in columns)
        west_right_6 = (row + 1 in rows and column + 7 in columns)
        west_right_7 = (row + 1 in rows and column + 8 in columns)
        if (west_right_1 and west_left_1) or (west_right_2 and west_left_2) or (west_right_3 and west_left_3) or \
                (west_right_4 and west_left_4) or (west_right_5 and west_left_5) or (west_right_6 and west_left_6) or \
                (west_right_7 and west_left_7):
            return (row,column)

    def double_deflection_east(self, row, column):
        """Returns interaction if there is a double deflection that occurs on right side of board"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        east_left_1 = (row+1 in rows and column-2 in columns)
        east_left_2 = (row+1 in rows and column-3 in columns)
        east_left_3 =(row+1 in rows and column-4 in columns)
        east_left_4 =(row+1 in rows and column-5 in columns)
        east_left_5 = (row+1 in rows and column-6 in columns)
        east_left_6 =(row+1 in rows and column-7 in columns)
        east_left_7 =(row+1 in rows and column-8 in columns)
        east_right_1 = (row - 1 in rows and column -2 in columns)
        east_right_2 = (row - 1 in rows and column -3 in columns)
        east_right_3 =(row - 1 in rows and column -4 in columns)
        east_right_4 = (row - 1 in rows and column -5 in columns)
        east_right_5 =(row - 1 in rows and column -6 in columns)
        east_right_6 = (row - 1 in rows and column - 7 in columns)
        east_right_7 = (row - 1 in rows and column -8 in columns)
        if (east_right_1 and east_left_1) or (east_right_2 and east_left_2) or (east_right_3 and east_left_3) or \
                (east_right_4 and east_left_4) or (east_right_5 and east_left_5) or (east_right_6 and east_left_6) or \
                (east_right_7 and east_left_7):
            return (row,column)

    def double_deflection_top(self, row, column):
        """Returns interaction if there is a double deflection that occurs on top side of board"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        top_right_1 = (column - 1 in columns and row + 2 in rows)
        top_right_2 = (column - 1 in columns and row + 3 in rows)
        top_right_3 = (column - 1 in columns and row + 4 in rows)
        top_right_4 = (column - 1 in columns and row + 5 in rows)
        top_right_5 = (column - 1 in columns and row + 6 in rows)
        top_right_6 = (column - 1 in columns and row + 7 in rows)
        top_right_7 = (column - 1 in columns and row + 8 in rows)
        top_left_1 = (column + 1 in columns and row + 2 in rows)
        top_left_2 = (column + 1 in columns and row + 3 in rows)
        top_left_3 = (column + 1 in columns and row + 4 in rows)
        top_left_4 = (column + 1 in columns and row + 5 in rows)
        top_left_5 = (column + 1 in columns and row + 6 in rows)
        top_left_6 = (column + 1 in columns and row + 7 in rows)
        top_left_7 = (column + 1 in columns and row + 8 in rows)
        if (top_left_1 and top_right_1) or (top_right_2 and top_left_2) or (top_right_3 and top_left_3) or \
                (top_right_4 and top_left_4) or (top_right_5 and top_left_5) or (top_right_6 and top_left_6) or \
                (top_right_7 and top_left_7):
            return (row, column)

    def double_deflection_bottom(self, row, column):
        """Returns interaction if there is a double deflection that occurs on bottom side of board"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        bottom_right_1 = (column + 1 in columns and row - 2 in rows)
        bottom_right_2 = (column + 1 in columns and row - 3 in rows)
        bottom_right_3 = (column + 1 in columns and row - 4 in rows)
        bottom_right_4 = (column + 1 in columns and row - 5 in rows)
        bottom_right_5 = (column + 1 in columns and row - 6 in rows)
        bottom_right_6 = (column + 1 in columns and row - 7 in rows)
        bottom_right_7 = (column + 1 in columns and row - 8 in rows)

        bottom_left_1 = (column - 1 in columns and row - 2 in rows)
        bottom_left_2 = (column - 1 in columns and row - 3 in rows)
        bottom_left_3 = (column - 1 in columns and row - 4 in rows)
        bottom_left_4 = (column - 1 in columns and row - 5 in rows)
        bottom_left_5 = (column - 1 in columns and row - 6 in rows)
        bottom_left_6 = (column - 1 in columns and row - 7 in rows)
        bottom_left_7 = (column - 1 in columns and row - 8 in rows)
        if (bottom_left_1 and bottom_right_1) or (bottom_right_2 and bottom_left_2) or \
                (bottom_right_3 and bottom_left_3) or (bottom_right_4 and bottom_left_4) or \
                (bottom_right_5 and bottom_left_5) or (bottom_right_6 and bottom_left_6) or \
                (bottom_right_7 and bottom_left_7):
            return (row, column)

    def detour_west(self,row,column):
        """Returns if the ray has a detour if ray shot from left side of board"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        var = ((column+2 in columns or column+3 in columns or column+4 in columns or column+5 in columns \
                or column+6 in columns or column+7 in columns))
        if (row ==2 or row==3 or row==4 or row==5 or row==6):
            if (row-1 in rows and var) and (row+2 in rows and var):
                return (row+1,column)
        if (row==2 or row==3 or row==4 or row==5):
            if (row - 1 in rows and var) and (row + 3 in rows and var):
                return (row + 2, column)
        if (row==2 or row==3 or row==4):
            if (row - 1 in rows and var) and (row + 4 in rows and var):
                return (row + 3, column)
        if (row==2 or row==3):
            if (row - 1 in rows and var) and (row + 5 in rows and var):
                return (row + 4, column)
        if row==2:
            if (row - 1 in rows and var) and (row + 6 in rows and var):
                return (row + 5, column)

    def detour_east(self,row,column):
        """Returns if the ray has a detour if ray shot from right side of board"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        var = ((column-2 in columns or column-3 in columns or column-4 in columns or column-5 in columns \
                or column-6 in columns or column-7 in columns))
        if (row ==7 or row==6 or row==5 or row==4 or row==3):
            if (row+1 in rows and var) and (row-2 in rows and var):
                return (row-1,column)
        if (row==7 or row==6 or row==5 or row==4):
            if (row - 1 in rows and var) and (row - 3 in rows and var):
                return (row - 2, column)
        if (row==7 or row==6 or row==5):
            if (row - 1 in rows and var) and (row - 4 in rows and var):
                return (row - 3, column)
        if (row==7 or row==6):
            if (row - 1 in rows and var) and (row - 5 in rows and var):
                return (row - 4, column)
        if row==7:
            if (row - 1 in rows and var) and (row - 6 in rows and var):
                return (row - 5, column)

    def detour_bottom(self, row, column):
        """Returns if the ray has a detour if ray shot from bottom side of board"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        var = ((row - 2 in rows or row - 3 in rows or row - 4 in rows or row - 5 in rows \
                or row - 6 in rows or row - 7 in rows))
        if (column == 2 or column == 3 or column == 4 or column == 5 or column == 6):
            if (column - 1 in columns and var) and (column + 2 in columns and var):
                return (row,column+1)
        if (column == 2 or column == 3 or column == 4 or column == 5):
            if (column - 1 in columns and var) and (column + 3 in columns and var):
                return (row , column+2)
        if (column == 2 or column == 3 or column == 4):
            if (column - 1 in columns and var) and (column + 4 in columns and var):
                return (row , column+3)
        if (column == 2 or column == 3):
            if (column- 1 in columns and var) and (column + 5 in columns and var):
                return (row, column+4)
        if column == 2:
            if (column - 1 in columns and var) and (column + 6 in columns and var):
                return (row , column+5)

    def detour_top(self, row, column):
        """Returns if the ray has a detour if ray shot from top side of board"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        var = ((row + 2 in rows or row + 3 in rows or row + 4 in rows or row + 5 in rows \
                or row + 6 in rows or row + 7 in rows))
        if (column == 7 or column == 6 or column == 5 or column == 4 or column == 3):
            if (column + 1 in columns and var) and (column - 2 in columns and var):
                return (row, column - 1)
        if (column == 7 or column == 6 or column == 5 or column == 4):
            if (column + 1 in columns and var) and (column - 3 in columns and var):
                return (row, column - 2)
        if (column == 7 or column == 6 or column == 5):
            if (column + 1 in columns and var) and (column - 4 in columns and var):
                return (row, column - 3)
        if (column == 7 or column == 6):
            if (column + 1 in columns and var) and (column - 5 in columns and var):
                return (row, column - 4)
        if column == 7:
            if (column + 1 in columns and var) and (column - 6 in columns and var):
                return (row, column - 5)

    def detour_helper(self,row,column):
        """Helper method for shoot_ray method that checks if there is detour of ray shot"""
        if self.detour_west(row, column):
            return self.detour_west(row, column)
        if self.detour_east(row,column):
            return self.detour_east(row,column)
        if self.detour_bottom(row,column):
            return self.detour_bottom(row,column)
        if self.detour_top(row,column):
            return self.detour_top(row,column)



    def helper_double(self,row,column):
        """Helper method for shoot_ray method, that returns output if there is double reflection"""
        if self.double_deflection_west(row, column):
            return self.double_deflection_west(row, column)
        if self.double_deflection_east(row, column):
            return self.double_deflection_east(row, column)
        if self.double_deflection_top(row, column):
            return self.double_deflection_top(row, column)
        if self.double_deflection_bottom(row, column):
            return self.double_deflection_bottom(row, column)

    def helper_deflection(self,row,column):
        """Helper method for shoot_ray method, that returns output if there ray is deflected"""
        if self.deflect_west_left(row, column):
            return self.deflect_west_left(row, column)
        if self.deflect_west_right(row, column):
            return self.deflect_west_right(row, column)
        if self.deflect_east_left(row, column):
            return self.deflect_east_left(row, column)
        if self.deflect_east_right(row, column):
            return self.deflect_east_right(row, column)
        if self.deflect_top_left(row, column):
            return self.deflect_top_left(row, column)
        if self.deflect_top_right(row, column):
            return self.deflect_top_right(row, column)
        if self.deflect_bottom_left(row, column):
            return self.deflect_bottom_left(row, column)
        if self.deflect_bottom_right(row, column):
            return self.deflect_bottom_right(row, column)



    def shoot_ray(self, row, column):
        """"Returns the direction/entrance coordinate/exit coordinate/pattern of the ray shot by taking the
         parameter of a list of (row,column)"""
        if self.hit_ray(row, column):
            return self.hit_ray(row, column)
        if self.miss_ray(row, column):  # if the ray misses, deduct 2 points
            self._score -= 2
            return self.miss_ray(row, column)
        if self.reflection_ray(row, column):
            self._score -= 1  # If the ray reflects, deduct 1 point
            return self.reflection_ray(row, column)
        if self.detour_helper(row,column):
            self._score-=2
            return self.detour_helper(row,column)
        if self.helper_deflection(row, column):
            self._score-=2
            return self.helper_deflection(row, column)
        if self.helper_double(row, column):
            self._score-=1
            return self.helper_double(row, column)




    def guess_atom(self, row, column):
        """"Returns whether or not the guess the user inputs is at that location, method takes parameters of row
        and column, then returns either True/False"""
        check_row = [i[0] for i in self._atom_location]
        check_column = [i[1] for i in self._atom_location]
        rows = set(check_row)
        columns = set(check_column)
        var = (row,column)
        if (row in rows) and (column in columns):  # if the guess location matches atom location
            self._score += 0  # zero points taken off
            self._atom_count += 1  # if guess is correct, add one to counter
            return True
        if var in self._guess:
            self._score +=0 # if guessed already, zero point deducted
        else:
            self._score -= 5  # if guess wrong, deduct 5 points
            return False

    def get_score(self):
        """Returns the current score of the game"""
        return self._score

    def atoms_left(self):
        """Returns the number of atoms that haven't been guessed yet"""
        # subtract total number of atoms by how many atoms guessed right
        return len(self._atom_location) - (self._atom_count)



