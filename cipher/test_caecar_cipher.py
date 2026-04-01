from caecar_cipher import caesarCipher
import unittest


class caesarCipherTest(unittest.TestCase):
    def test_give_middleOutz_with_k2_return_okffngQwvb(self):
        s = "middle-Outz"
        result = caesarCipher(s, 2)
        self.assertEqual(result, "okffng-Qwvb")

    def test_give_long_text(self):
        s = "Always-Look-on-the-Bright-Side-of-Life"
        result = caesarCipher(s, 5)
        self.assertEqual(result, "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj")

    def test_give_more_than_26(self):
        s = "www.abc.xy"
        result = caesarCipher(s, 87)
        self.assertEqual(result, "fff.jkl.gh")
