import unittest
import lib
class LibTest(unittest.TestCase):
    def test_prime_non_negative_arg(self):
        self.assertEqual(lib.prime(1),False)
        self.assertEqual(lib.prime(2),True)
        self.assertEqual(lib.prime(0),False)
        self.assertEqual(lib.prime(7),True)
    def test_prime_negative(self):
        self.assertEqual(lib.prime(-1),False)
        self.assertEqual(lib.prime(-2),False)
       
unittest.main(verbosity=2)
