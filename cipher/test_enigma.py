import unittest
import random
import string
from enigma import Enigma


class TestEnigma(unittest.TestCase):

    def test_default_encode_decode(self):
        '''
        Creates a 20 char long word. Cipher and decipher this message with
        default parameters. If ciphered and original word different and deciphered
        and original word is same as deciphered word, test is passed.
        '''
        all_letters = string.ascii_letters + '''0 123/45\t6\n789.,?!:"';'''
        cipher = Enigma()

        for _ in range(50):
            word = random.choices(all_letters, k=20)
            word = ''.join(word)
            encoded = cipher.cipher(word)
            decoded = cipher.decipher(encoded)
            self.assertNotEqual(encoded, word)
            self.assertEqual(word, decoded)

    def test_rotor_encode_decode(self):
        '''
        Creates a 20 char long word. Cipher and decipher this message with
        random rotor selections. If ciphered and original word different and
        deciphered and original word is same as deciphered word, test is passed.
        '''
        all_letters = string.ascii_letters + '''0 123/45\t6\n789.,?!:"';'''

        for _ in range(50):
            rotors = random.choices(range(10), k=3)
            cipher = Enigma(rotors=rotors)

            word = random.choices(all_letters, k=20)
            word = ''.join(word)
            encoded = cipher.cipher(word)
            decoded = cipher.decipher(encoded)
            self.assertNotEqual(encoded, word)
            self.assertEqual(word, decoded)

    def test_plugboards_encode_decode(self):
        '''
        Creates a 20 char long word. Cipher and decipher this message with
        random plugboard selections. If ciphered and original word different
        and deciphered and original word is same as deciphered word, test is passed.
        '''
        all_letters = string.ascii_letters + '''0 123/45\t6\n789.,?!:"';'''

        for _ in range(50):
            plugboards = random.choices(range(10), k=2)
            cipher = Enigma(plugboards=plugboards)

            word = random.choices(all_letters, k=20)
            word = ''.join(word)
            encoded = cipher.cipher(word)
            decoded = cipher.decipher(encoded)
            self.assertNotEqual(encoded, word)
            self.assertEqual(word, decoded)

    def test_offsets_encode_decode(self):
        '''
        Creates a 20 char long word. Cipher and decipher this message with
        random offset selections. If ciphered and original word different
        and deciphered and original word is same as deciphered word, test is passed.
        '''
        all_letters = string.ascii_letters + '''0 123/45\t6\n789.,?!:"';'''

        for _ in range(50):
            offsets = random.choices(range(len(all_letters)), k=3)
            cipher = Enigma(offsets=offsets)

            word = random.choices(all_letters, k=20)
            word = ''.join(word)
            encoded = cipher.cipher(word)
            decoded = cipher.decipher(encoded)
            self.assertNotEqual(encoded, word)
            self.assertEqual(word, decoded)


if __name__ == '__main__':
    unittest.main()
