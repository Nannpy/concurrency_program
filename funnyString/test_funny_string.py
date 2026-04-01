from funny_string import funnyString
import unittest


class FunnyStringTest(unittest.TestCase):
    def test_give_acxz_is_funny(self):
        s = "acxz"
        result = funnyString(s)
        self.assertEqual(result, "Funny")

    def test_give_bcxz_is_not_funny(self):
        s = "bcxz"
        result = funnyString(s)
        self.assertEqual(result, "Not Funny")

    def test_give_ivvkxq_is_not_funny(self):
        s = "ivvkxq"
        result = funnyString(s)
        self.assertEqual(result, "Not Funny")

    def test_give_ivvkx_is_not_funny(self):
        s = "ivvkx"
        result = funnyString(s)
        self.assertEqual(result, "Not Funny")
