from TwoCharacter import alternate
import unittest


class alternateTest(unittest.TestCase):
    def test_1(self):
        s = "beabeefeab"
        result = alternate(s)
        self.assertEqual(result, 5)

    def test_2(self):
        s = "asdcbsdcagfsdbgdfanfghbsfdab"
        result = alternate(s)
        self.assertEqual(result, 8)

    def test_3(self):
        s = "asvkugfiugsalddlasguifgukvsa"
        result = alternate(s)
        self.assertEqual(result, 0)
