from stack import Stack

class Hanoi:
    """
    A class which implement the hanoi tower game.
    """
    
    def __init__(self, n):
        self._tower1 = Stack()
        self._tower2 = Stack()
        self._tower3 = Stack()
        self._size = n
        self._history = []
        self._create()
    
    
    def move(self, src, dest):
        """
        Move the plate from src to dest
        src : integer {1, 2, 3}
        dest : integer {1, 2, 3}
        Return a status :
            0 : success of the movement, (src, dest)
            1 : game over, (src, dest)
            2 : the top plate of the src is larger than the top plate of the dest, (src, dest)
            3 : source and destination are the same, (src, src)
            4 : tried to pop an empty tower, ()
            5 : invalid value, ()
        """
        mapping = {1 : self._tower1, 2 : self._tower2, 3 : self._tower3}
        
        if src not in (1, 2, 3) or dest not in (1, 2, 3):  # invalid value
            return 5, ()  
        if mapping[src].isEmpty():  # tried to pop an empty tower
            return 4, ()  
        if src == dest:  # source and destination are the same
            return 3, (src, src)  
        if not mapping[dest].isEmpty() and mapping[src].summit() > mapping[dest].summit():
            # if the destination is not empty and
            # if the top plate of the source is larger than the top plate of the destination
            return 2, (src, dest)
        
        else:  
            # If the move should be valid
            # Then move the plate from src to dest
            mapping[dest].push(mapping[src].pop())
            if mapping[3].size() == self._size:  # Game over
                return 1, (src, dest)  
            else:  # Success of this movement
                return 0, (src, dest)  
    
    
    def show(self):
        """
        Show the game
        Return a tuple of 3 tuples. Example : ((2,3), (), (1))
        """
        return (self._tower1.show(), self._tower2.show(), self._tower3.show())
    
    def _create(self):
        """
        Create each plate and push them in _tower1
        """
        # TODO : check that n is in [3:10] ??
        for i in range(self._size, 0, -1):
            self._tower1.push(i)