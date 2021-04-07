import unittest
import random
import string
from polycipher import PolyCipher


class TestPolyCipher(unittest.TestCase):

    def test_encode_letters(self):
        '''
        Testing every latin letters encoding. With current mask encoded letter cannot be itself
        after encoding. So if encoded letter is different than original letter test is passed. 
        '''
        letters = string.ascii_letters
        cipher = PolyCipher()

        for letter in letters:
            self.assertNotEqual(cipher.encode(letter), letter)

    def test_encode_numbers(self):
        '''
        Testing every number encoding. With current mask encoded letter cannot be itself
        after encoding. So if encoded number is different than original number test is passed. 
        '''
        numbers = '0123456789'
        cipher = PolyCipher()

        for number in numbers:
            self.assertNotEqual(cipher.encode(number), number)

    def test_encode_punctuations(self):
        '''
        Testing every punctuations encoding. With current mask encoded punctuation cannot be itself
        after encoding. So if encoded punctuation is different than original punctuation test is passed. 
        '''
        punctuations = ''',./?;'"!'''
        cipher = PolyCipher()

        for punc in punctuations:
            self.assertNotEqual(cipher.encode(punc), punc)

    def test_encode_spaces(self):
        '''
        Testing every type of space encoding. With current mask encoded space cannot be itself
        after encoding. So if encoded space is different than original space test is passed. 
        '''
        spaces = ' \t\n'
        cipher = PolyCipher()

        for space in spaces:
            self.assertNotEqual(cipher.encode(space), space)

    def test_encode_combined(self):
        '''
        Testing every 3 char long random words encoding. 50 times it compares original word and 
        encoded word. If encoded word is different than original word test is passed. 
        '''
        all_letters = string.ascii_letters + '''0 123/45\t6\n789.,?!:"';'''
        cipher = PolyCipher()

        for _ in range(50):
            word = random.choices(all_letters, k=3)
            word = ''.join(word)

            self.assertNotEqual(cipher.encode(word), word)

    def test_encode_empty(self):
        '''
        Test if empyty string input for decoding raises AssertionError.
        '''
        cipher = PolyCipher()

        with self.assertRaises(AssertionError):
            cipher.encode('')

    def test_decode_letters(self):
        '''
        Testing every latin letters decoding. With current mask encoded letter cannot be itself
        after decoding. So if encoded letter is different than decoded letter test is passed. 
        '''
        letters = string.ascii_letters
        cipher = PolyCipher()

        for letter in letters:
            self.assertNotEqual(cipher.decode(letter), letter)

    def test_decode_numbers(self):
        '''
        Testing every number decoding. With current mask decoded letter cannot be itself
        after decoding. So if encoded number is different than decoded number test is passed. 
        '''
        numbers = '0123456789'
        cipher = PolyCipher()

        for number in numbers:
            self.assertNotEqual(cipher.decode(number), number)

    def test_decode_punctuations(self):
        '''
        Testing every punctuations decoding. With current mask decoded punctuation cannot be itself
        after decoding. So if encoded punctuation is different than decoded punctuation test is passed. 
        '''
        punctuations = ''',./?;'"!'''
        cipher = PolyCipher()

        for punc in punctuations:
            self.assertNotEqual(cipher.decode(punc), punc)

    def test_decode_spaces(self):
        '''
        Testing every type of space decoding. With current mask decoded space cannot be itself
        after decoding. So if encoded space is different than decoded space test is passed. 
        '''
        spaces = ' \t\n'
        cipher = PolyCipher()

        for space in spaces:
            self.assertNotEqual(cipher.encode(space), space)

    def test_decode_combined(self):
        '''
        Testing every 3 char long random words decoding. 50 times it compares encoded word and 
        decoded word. If decoded word is different than encoded word test is passed. 
        '''
        all_letters = string.ascii_letters + '''0 123/45\t6\n789.,?!:"';'''
        cipher = PolyCipher()

        for _ in range(50):
            word = random.choices(all_letters, k=3)
            word = ''.join(word)

            decoded = cipher.decode(word)
            self.assertNotEqual(decoded, word)

    def test_decode_empty(self):
        '''
        Test if empyty string input for encoding raises AssertionError.
        '''
        cipher = PolyCipher()

        with self.assertRaises(AssertionError):
            cipher.decode('')

    def test_encode_decode(self):
        '''
        3 char long random words tested for correct encode and decode of a word.
        Every word is encoded than decoded. If original word and decoded word is
        same test and encoded word and decoded words are different is passed.
        This repeated 50 times with random word creation.
        '''
        all_letters = string.ascii_letters + '''0 123/45\t6\n789.,?!:"';'''
        cipher = PolyCipher()

        for _ in range(50):
            word = random.choices(all_letters, k=3)
            word = ''.join(word)

            encoded = cipher.encode(word)
            decoded = cipher.decode(encoded)

            self.assertNotEqual(encoded, word)
            self.assertEqual(word, decoded)


# Test can be directly run as python file 
if __name__ == '__main__':
    unittest.main()