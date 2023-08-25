from checker import Checker
from board_cell import BoardCell
# CONSTANTS
BLACK_HUMAN = (10, 10, 10)
RED_COMPUTER = (250, 0, 0)
BROWN = (224, 191, 153)
YELLOW = (114, 68, 12)
HUMAN = "human"
COMPUTER = "computer"


class ChessBoard():
    """set up chess board"""
    def __init__(self, cell_size, board_size, crown):
        """constructor for the board"""

        self.board_colors = [YELLOW, BROWN]
        self.board_size = board_size
        self.cell_size = cell_size
        self.board = []
        self.current_checker = None
        self.frozen = False
        self.jumps = 0

        # a list of checkers with x and y of their position,
        # and whether it belongs to human or computer
        self.checkers_black = []
        self.checkers_red = []
        self.moves = 0

        for i in range(self.board_size):
            self.board.append(list())
            for j in range(self.board_size):
                color = self.board_colors[(j + 1) % 2]
                if i % 2 == 1:
                    color = self.board_colors[j % 2]

                self.board[i].append(BoardCell(
                    i * self.cell_size,
                    j * self.cell_size,
                    self.cell_size,
                    color
                ))
        for i in range(5, 8):
            print("i", i)
            if i % 2 == 1:
                j = 0
            else:
                j = 1
            while j < 8:
                print("j", j)
                self.checkers_black.append(
                    Checker(j, i, HUMAN, BLACK_HUMAN, cell_size, crown))
                j += 2
        for i in range(0, 3):
            if i % 2 == 1:
                j = 0
            else:
                j = 1
            while j < 8:
                self.checkers_red.append(
                    Checker(j, i, COMPUTER, RED_COMPUTER, cell_size, crown))
                j += 2

    def update(self, mouse_pressed, x=None, y=None):
        # update board
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.board[i][j].update()

        # update black checkers
        for chr in self.checkers_black:
            # update blacker checker except the current one.
            if chr is not self.current_checker:
                chr.update()

        # update red checkers
        for chr in self.checkers_red:
            chr.update()

        # the current checker, which is being dragged by the mouse
        if self.current_checker is not None:
            self.current_checker.update(x, y)

    def move_checker(self, checker, x, y):
        """move checkers, for computer player"""
        # first get the list of achievable positions
        checker.move(x, y)
        self.king(checker)
        self.moves += 1

    def jumpable(self, checker):
        """return a list of cells the checker can jump based on player"""
        jumpable_list = []
        check_list = self.checkers_black
        if checker is None:
            return jumpable_list
        if checker.player == HUMAN:
            check_list = self.checkers_red
        for i in range(self.board_size):
            for j in range(self.board_size):
                new_x = -1
                new_y = -1
                if checker.is_king:
                    if abs(checker.x - i) == 2 and abs(checker.y - j) == 2:
                        new_x = (checker.x + i) // 2
                        new_y = (checker.y + j) // 2
                elif checker.player == HUMAN:
                    if checker.y - j == 2 and abs(checker.x - i) == 2:
                        new_x = (checker.x + i) // 2
                        new_y = (checker.y + j) // 2
                elif checker.player == COMPUTER:
                    if checker.y - j == -2 and abs(checker.x - i) == 2:
                        new_x = (checker.x + i) // 2
                        new_y = (checker.y + j) // 2
                for c in check_list:
                    if c.x == new_x and c.y == new_y:
                        jumpable_list.append([i, j])
        for c in self.checkers_black:
            x = c.x
            y = c.y
            if [x, y] in jumpable_list:
                jumpable_list.remove([x, y])
        for c in self.checkers_red:
            x = c.x
            y = c.y
            if [x, y] in jumpable_list:
                jumpable_list.remove([x, y])
        return jumpable_list

    def achievable(self, checker):
        """return a list of achievable cells for checker and based on player"""
        achievable_list = []
        if checker is None:
            return achievable_list
        for i in range(self.board_size):
            for j in range(self.board_size):
                if checker.is_king:
                    if abs(checker.x - i) == 1 and abs(checker.y - j) == 1:
                        achievable_list.append([i, j])
                elif checker.player == HUMAN:
                    if checker.y - j == 1 and abs(checker.x - i) == 1:
                        achievable_list.append([i, j])
                elif checker.player == COMPUTER:
                    if checker.y - j == -1 and abs(checker.x - i) == 1:
                        achievable_list.append([i, j])
        for c in self.checkers_black:
            x = c.x
            y = c.y
            if [x, y] in achievable_list:
                achievable_list.remove([x, y])
        for c in self.checkers_red:
            x = c.x
            y = c.y
            if [x, y] in achievable_list:
                achievable_list.remove([x, y])
        return achievable_list

    def delete_checker(self, checker):
        """delete a checker from list"""
        if checker in self.checkers_red:
            self.checkers_red.remove(checker)
        if checker in self.checkers_black:
            self.checkers_black.remove(checker)

    def king(self, checker):
        """make a checker into king"""
        if ((checker.player == HUMAN and checker.y == 0) or
                (checker.player == COMPUTER
                    and checker.y == (self.board_size - 1))):
            checker.is_king = True

    def place_checker(self, x, y):
        """place the current checker to a cell"""
        valid = self.is_valid_move(x, y)
        if valid == 0:
            self.current_checker = None
            return

        if self.current_checker is None:
            return

        old_x = self.current_checker.x
        old_y = self.current_checker.y

        board_x, board_y = self.pixel_to_index(x, y)
        self.current_checker.move(board_x, board_y)
        self.king(self.current_checker)
        check_list = self.checkers_black
        if self.current_checker.player == HUMAN:
            check_list = self.checkers_red
        if valid == 2:
            new_x = (old_x + board_x) // 2
            new_y = (old_y + board_y) // 2
            for c in check_list:
                if c.x == new_x and c.y == new_y:
                    self.delete_checker(c)
                    self.jumps += 1
                    break
        self.moves += 1
        self.current_checker = None

    def is_valid_move(self, x, y):
        """
        validate whether the current release position is a valid position,
        call achievable() to get a list of valid position and call jumpable()
        to get a list of valid position that can jump to check the current
        position is valid
        """
        b_x, b_y = self.pixel_to_index(x, y)
        achievable_list = self.achievable(self.current_checker)
        jump_list = self.jumpable(self.current_checker)
        if [b_x, b_y] in achievable_list:
            return 1
        elif [b_x, b_y] in jump_list:
            return 2
        return 0

    def pixel_to_index(self, x, y):
        """get the indices of x and y from the pixel"""
        return x // self.cell_size, y // self.cell_size

    def pick_checker(self, x, y):
        """pick the checker by mouse"""
        self.current_checker = self.find_checker_at_pos(x, y)

    def find_checker_at_pos(self, x, y):
        board_x, board_y = self.pixel_to_index(x, y)
        for chr in self.checkers_black:
            if chr.x == board_x and chr.y == board_y:
                return chr
        return None
