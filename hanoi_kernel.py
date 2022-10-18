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
        self._create()
    
    
    def move(self, src, dest):
        """
        Move the plate from src to dest
        src : integer {1, 2, 3}
        dest : integer {1, 2, 3}
        Return a status :
        - 0 : success
        - 1 : forbiden move
        - 2 : pop an empty tower
        """
        mapping = {1 : self._tower1, 2 : self._tower2, 3 : self._tower3}
        if mapping[dest].isEmpty() or summit(mapping[src]) < summit(mapping[dest]):
            # If destination is empty
            # or if the top plate of the destination is larger than the top plate of the source
            # Then move the plate from src to dest
            try:
                mapping[dest].push(mapping[src].pop())
                self.counter += 1
                return 0  # Success
            except IndexError:
                # If the source list is empty
                return -2  # Error : tried to pop an empty tower
            
    
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
        # TODO : check that n is in [3:10]
        for i in range(6, 0, -1):
            self._tower1.push(i)