
class Checker():

    def __init__(self, x, y, player, color, CELL_SIZE, king_image):
        """constructor"""
        # CONSTANTS
        self.CELL_SIZE = CELL_SIZE
        self.king_image = king_image
        self.OUTER_SIZE = 0.9
        self.INNER_SIZE = 0.7
        # variables
        self.color = color
        self.x = x
        self.y = y
        self.player = player
        self.is_king = False

    def update(self, x=None, y=None):
        """
        Display the checker disk at given position (x, y)
        """
        # CONSTANTS
        STROKE_WEIGHT = 2
        STROKE_COLOR = 255
        # Checker's setting
        fill(*self.color)
        strokeWeight(STROKE_WEIGHT)
        stroke(STROKE_COLOR)

        if x is None and y is None:
            center_x = self.x*self.CELL_SIZE + self.CELL_SIZE / 2
            center_y = self.y*self.CELL_SIZE + self.CELL_SIZE / 2
            circle(center_x, center_y, self.OUTER_SIZE*self.CELL_SIZE)
            circle(center_x, center_y, self.INNER_SIZE*self.CELL_SIZE)
            center_x -= self.CELL_SIZE / 4
            center_y -= self.CELL_SIZE / 4
            if self.is_king:
                image(self.king_image, center_x, center_y)
        else:
            circle(x, y, self.OUTER_SIZE*self.CELL_SIZE)
            circle(x, y, self.INNER_SIZE*self.CELL_SIZE)
            if self.is_king:
                image(self.king_image, x - self.CELL_SIZE / 4,
                      y - self.CELL_SIZE / 4)

    def move(self, x, y):
        """update the positon of the checker"""
        self.x = x
        self.y = y

    def is_king(self):
        """check if a checker is king"""
        return self.is_king

    def set_to_king(self):
        self.is_king = True
