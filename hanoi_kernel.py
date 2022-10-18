from stack import Stack

class Hanoi:
    """
    A class which implement the hanoi tower game.
    """
    
    def __init__(self, n):
        self._tower1 = Stack()
        self._tower2 = Stack()
        self._tower3 = Stack()
        self._counter = 0
        self._create(n)
    
    def move(self, src, dest):
        """
        Move the plate from src to dest
        src : integer {1, 2, 3}
        dest : integer {1, 2, 3}
        Return ??? TODO
        """
        pass
    
    def show(self):
        """
        Show the game
        Return a tuple of 3 tuples. Example : ((2,3), (), (1))
        """
        pass
    
    def _create(self):
        # TODO : check that n is in [3:10]
        pass