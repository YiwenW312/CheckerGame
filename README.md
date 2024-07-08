# The Game of Checkers - Backend Python Application with GUI
A final project - Checker Game in python, using processing for CS5001 Intensive Foundations of CS in Spring 2023

# Project Overview
- Developed an interactive 2-player chess game in Python with a GUI using the Processing library, implementing comprehensive chess rules and an intuitive drag-and-drop interface.

- Role: Developer

- Technologies Used: Python, Processing

# Key Contributions and Achievements
- Developed the game logic and GUI, ensuring smooth gameplay and visual feedback for users.
- Implementing complex game rules and providing visual hints for potential moves.
- Enhanced user experience with visual hints for potential moves and automatic detection of check and checkmate scenarios.

# Summary

This project is a graphical game of Checkers in **Python/Processing**, from scratch. 


Checkers is a two-person abstract strategy game played with colored disks called checkers on an identical board to a chess board. On each player's turn, a piece may be moved diagonally to an empty space, or if an opponent's piece occupies one space diagonally from the piece to play, and the next space in the same direction is empty, then the piece may jump over the opponent's piece and capture it. Captured pieces are removed from the board. The objective is to be the last player with pieces on the board.


A few additional rules are as follows:
1. Pieces may move in a forward diagonal direction only, both for single moves and for jumps. They cannot move in a backward diagonal direction. However, once they reach the opposite edge of the board they become "king" pieces. King pieces may move forward diagonally or backward diagonally, both for single moves and for jumps.
2. If a jump opportunity presents itself, the jump must be taken. If more than one jump opportunity presents itself at once, then the player can choose which jump to make. If multiple jumps can be made in sequence with the same piece, all possible jumps must be made, resulting in double or triple (or more) jumps.
3. If a player is unable to make a legal move, that player loses.
4. If 50 moves pass without any jumps occurring, the result is a draw.

![Board Demo](https://github.com/YiwenW312/CheckerGame/blob/main/checkergameDemo.png)
