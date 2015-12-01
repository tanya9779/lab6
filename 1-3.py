import unittest
import lib
class LibTest(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(lib.palindrome('арозаупаланалапуазора'),True)
        self.assertEqual(lib.palindrome('мамамылараму'),False)
        self.assertEqual(lib.palindrome('1221'),True)
        self.assertEqual(lib.palindrome('001'),False)
        self.assertEqual(lib.palindrome('1221'),True)
        self.assertEqual(lib.palindrome('0'),True)
        self.assertEqual(lib.palindrome('-1'),False)
        self.assertEqual(lib.palindrome(''),True)
    
       
unittest.main(verbosity=2)
