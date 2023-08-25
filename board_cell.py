class BoardCell:
    """draw a boardcell"""
    def __init__(self, x, y, cell_size, color):
        """constructor"""
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.color = color

    def update(self):
        noStroke()

        fill(*self.color)
        rect(self.x, self.y, self.cell_size, self.cell_size)
