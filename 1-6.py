import unittest
import lib
class LibTest(unittest.TestCase):
    def test_sqrt_non_negative_arg(self):
        self.assertEqual(lib.sqrt(4),2)
        self.assertEqual(lib.sqrt(1),1)
        self.assertEqual(lib.sqrt(0),0)

    def test_factorial_negative(self):
        self.assertEqual(lib.sqrt(-1),0)
       
unittest.main(verbosity=2)
