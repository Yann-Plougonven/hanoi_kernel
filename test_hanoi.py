import unittest
from hanoi_kernel import Hanoi

class HanoiTests(unittest.TestCase):
    """
    A class to test hanoi's kernel
    """
    
    def setUp(self):
        self.hanoi = Hanoi(3)
    
    def testHanoiStatus0(self):
        """success of the movement"""
        status, move = self.hanoi.move(1,3)
        expected_status = 0
        self.assertEqual(status, expected_status, f"Status should be {expected_status}, but is {status}")
        expected_move = 1,3
        self.assertEqual(move, expected_move, f"Move should be {expected_move}, but is {move}")
        
    def testHanoiStatus1(self):
        """game over"""
        hanoi = Hanoi(1)
        status, move = hanoi.move(1,3)
        expected_status = 1
        self.assertEqual(status, expected_status, f"Status should be {expected_status}, but is {status}")
        expected_move = 1,3
        self.assertEqual(move, expected_move, f"Move should be {expected_move}, but is {move}")
        
    def testHanoiStatus2(self):
        """the top plate of the src is larger than the top plate of the dest"""
        status, move = self.hanoi.move(1,3)
        expected_status = 0
        self.assertEqual(status, expected_status, f"Status should be {expected_status}, but is {status}")
        expected_move = 1,3
        self.assertEqual(move, expected_move, f"Move should be {expected_move}, but is {move}")
            
        
# TODO
#     def testHanoiStatus3(self):
#         """source and destination are the same"""
#         status, move = self.hanoi.move(1,3)
#         expected_status = 0
#         self.assertEqual(status, expected_status, f"Status should be {expected_status}, but is {status}")
#         expected_move = 1,3
#         self.assertEqual(move, expected_move, f"Move should be {expected_move}, but is {move}")
# 
#     def testHanoiStatus4(self):
#         """tried to pop an empty tower"""
#         status, move = self.hanoi.move(1,3)
#         expected_status = 0
#         self.assertEqual(status, expected_status, f"Status should be {expected_status}, but is {status}")
#         expected_move = 1,3
#         self.assertEqual(move, expected_move, f"Move should be {expected_move}, but is {move}")
#         
#     def testHanoiStatus5(self):
#         """invalid value"""
#         status, move = self.hanoi.move(1,3)
#         expected_status = 0
#         self.assertEqual(status, expected_status, f"Status should be {expected_status}, but is {status}")
#         expected_move = 1,3
#         self.assertEqual(move, expected_move, f"Move should be {expected_move}, but is {move}")


def testHanoiSolve(self):
        _object = Hanoi(0)
        tour = _object.solve_hanoi(4)
        print(f"len = {len(tour.get_history())}")
        expected_result = ((), (), (4, 3, 2, 1))
        self.assertEqual(tour.show(), expected_result, f"Result should be {expected_result}, but is {tour.show()}")
        expected_number_of_moves = 15
        self.assertEqual(len(tour.get_history()), expected_number_of_moves, f"Number of moves should be {expected_number_of_moves}, but is {len(tour.get_history())}")

        
if __name__ == '__main__':
    unittest.main()