import random


class GameManager():

    def __init__(self, chess_board):
        self.result = ""
        self.chess_board = chess_board
        self.human_playing = True

    def switch(self):
        """switch side"""
        human = self.human_playing
        if human:
            self.human_playing = not self.human_playing
            self.computer_make_move()
        else:
            self.human_playing = not self.human_playing
        self.chess_board.frozen = not self.chess_board.frozen

    def computer_make_move(self):
        """the computer will use this method to move checkers"""
        jumpable_list, achievable_list = self.computer_can_move()
        if len(jumpable_list) == 0 and len(achievable_list) == 0:
            return
        if len(jumpable_list) > 0:
            idx = random.randint(0, len(jumpable_list) - 1)
            checker = jumpable_list[idx]
            cur_list = self.chess_board.jumpable(checker)
            coor = cur_list[random.randint(0, len(cur_list) - 1)]
            new_x = (checker.x + coor[0]) // 2
            new_y = (checker.y + coor[1]) // 2
            self.chess_board.move_checker(checker, coor[0], coor[1])
            for c in self.chess_board.checkers_black:
                if c.x == new_x and c.y == new_y:
                    self.chess_board.checkers_black.remove(c)
                    self.chess_board.jumps += 1
                    break
        else:
            idx = random.randint(0, len(achievable_list) - 1)
            checker = achievable_list[idx]
            cur_list = self.chess_board.achievable(checker)
            coor = cur_list[random.randint(0, len(cur_list) - 1)]
            self.chess_board.move_checker(checker, coor[0], coor[1])
        print(self.check_win())
        self.switch()

    def computer_can_move(self):
        """return lists of positions that computer's checkers can move or jump"""
        checker_list = self.chess_board.checkers_red
        jumpable_list = []
        achievable_list = []
        for c in checker_list:
            if len(self.chess_board.jumpable(c)) > 0:
                jumpable_list.append(c)
            if len(self.chess_board.achievable(c)) > 0:
                achievable_list.append(c)
        return jumpable_list, achievable_list

    def check_win(self):
        """check whether the game is draw or either side of the player wins"""
        result = -1
        if self.chess_board.moves >= 50 and self.chess_board.jumps == 0:
            result = 0
        if len(self.chess_board.checkers_red) == 0:
            result = 1
        else:
            can_move = False
            for c in self.chess_board.checkers_red:
                if len(self.chess_board.jumpable(c)) > 0:
                    can_move = True
                if len(self.chess_board.achievable(c)) > 0:
                    can_move = True
            if not can_move:
                result = 1

        if len(self.chess_board.checkers_black) == 0:
            result = 2
        else:
            can_move = False
            for c in self.chess_board.checkers_black:
                if len(self.chess_board.jumpable(c)) > 0:
                    can_move = True
                if len(self.chess_board.achievable(c)) > 0:
                    can_move = True
            if not can_move:
                result = 2
        if result == 1:
            print("human won")
        elif result == 2:
            print("computer won")
        return result
