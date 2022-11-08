class Pieces:
    """This class is for the 4 red and blue pawns and 1 red and blue king and will contain the following information: board location and status (alive vs. dead)"""

    def __init__(self, x_location, y_location, status):
        """initailize the starting location in x and y, along with the status as alive"""
        self.x = x_location
        self.y = y_location
        self.status = status

class Red_pieces(Pieces):

    def __init__(self,x_location, y_location, status):
        super().__init__(x_location, y_location, status)


    def move_r(self,):
