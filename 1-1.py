import unittest
import lib
class LibTest(unittest.TestCase):
    def test_even_non_negative_arg(self):
        self.assertEqual(lib.even(1),False)
        self.assertEqual(lib.even(2),True)
        self.assertEqual(lib.even(0),True)

    def test_even_negative(self):
        self.assertEqual(lib.even(-1),False)
        self.assertEqual(lib.even(-2),True)
unittest.main(verbosity=2)
