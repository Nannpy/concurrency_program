from alternateChar import alternatingCharacters
import unittest


class alternateCharTest(unittest.TestCase):
    def test_give_AAAA_return_3(self):
        s = "AAAA"
        result = alternatingCharacters(s)
        self.assertEqual(result, 3)

    def test_give_BBBBB_return_4(self):
        s = "BBBBB"
        result = alternatingCharacters(s)
        self.assertEqual(result, 4)

    def test_give_ABABABAB_return_0(self):
        s = "ABABABAB"
        result = alternatingCharacters(s)
        self.assertEqual(result, 0)

    def test_give_AAABBB_return_4(self):
        s = "AAABBB"
        result = alternatingCharacters(s)
        self.assertEqual(result, 4)
