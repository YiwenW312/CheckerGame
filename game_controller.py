from game_manager import GameManager


class GameController():
    """A gamecontroller for chess game"""

    def __init__(self, chess_board):
        """constructor"""
        self.game_manager = GameManager(chess_board)
        self.chess_board = chess_board

    def update(self, mouse_pressed, mouse_x, mouse_y):
        self.chess_board.update(mouse_pressed, mouse_x, mouse_y)
        if self.game_manager.check_win() == 0:
            fill(1)
            textSize(100)
            text("DRAW", 265, 500)
        elif self.game_manager.check_win() == 1:
            fill(1)
            textSize(100)
            text("BLACK WINS", 265, 500)
        elif self.game_manager.check_win() == 2:
            fill(1)
            textSize(100)
            text("RED WINS", 265, 500)

    def place_checker(self, mouse_x, mouse_y):
        moves = self.chess_board.moves
        self.chess_board.place_checker(mouse_x, mouse_y)
        result = -1
        if self.chess_board.moves == moves + 1:
            result = self.game_manager.switch()
            self.game_manager.check_win()

    def pick_checker(self, mouse_x, mouse_y):
        if not self.chess_board.frozen:
            self.chess_board.pick_checker(mouse_x, mouse_y)

    def end_game(self, result):
        # print(result)
        if result == "human_lose" or result == "human_win":
            fill(1)
            textSize(3000)
            text("Test",
                 100, 100)

    def display_end_text(self):
        pass
