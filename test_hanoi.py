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
        
        
if __name__ == '__main__':
    unittest.main()