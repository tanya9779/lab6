import unittest
import lib
import math
class LibTest(unittest.TestCase):
    def test_sin_non_negative_arg(self):
        self.assertEqual(lib.sin(0),0)
        self.assertEqual(lib.sin(math.pi/6),0.5)
        self.assertEqual(lib.sin(math.pi/2),1)
        self.assertEqual(lib.sin(math.pi),0)
    def test_sin_negative(self):
        self.assertEqual(lib.sin(-math.pi/6),-0.5)
        
       
unittest.main(verbosity=2)
