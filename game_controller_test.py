from game_controller import GameController
from chess_board import ChessBoard


def test_constructor():
    board = ChessBoard(120, 8, "crown")
    gc = GameController(board)
    assert gc.chess_board.board_size == 8
