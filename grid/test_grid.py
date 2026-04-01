from grid import gridChallenge
import unittest


class gridChallengeTest(unittest.TestCase):
    def test_1(self):
        s = ["eabcd", "fghij", "olkmn", "trpqs", "xywuv"]
        result = gridChallenge(s)
        self.assertEqual(result, "YES")

    def test_2(self):
        s = ["abc", "lmp", "qrt"]
        result = gridChallenge(s)
        self.assertEqual(result, "YES")

    def test_3(self):
        s = ["mpxz", "abcd", "wlmf"]
        result = gridChallenge(s)
        self.assertEqual(result, "NO")

    def test_4(self):
        s = ["abc", "hjk", "mpq", "rtv"]
        result = gridChallenge(s)
        self.assertEqual(result, "YES")
