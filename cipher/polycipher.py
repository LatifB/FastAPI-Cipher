from math import ceil
from collections import deque
import string


class PolyCipher():
    '''
    Python implementation of Polyalphabetic Cipher. A mask of matching size created from the key.
    Then letters from given string are shifted accourding to corresponding index of letters from mask
    to minimize fingerprint
    '''

    def __init__(self):
        self.letters = string.ascii_letters + '''0 123/45\t6\n789.,?!:"';'''
        self.letter2index = {}
        self.index2letter = {}
        self.key = 'CoMpUtEr'

        for i, letter in enumerate(self.letters):
            self.letter2index[letter] = i
            self.index2letter[i] = letter

    def encode(self, word):
        '''Encodes given string. Every charachter in the given word
        shifted accourding to corresponding letters index from the mask'''

        assert len(word) > 0, ValueError('Empty String')

        mask = self.__get_mask(word)

        mask = [self.letter2index[letter] for letter in mask]
        word = [self.letter2index[letter] for letter in word]

        cipher = [(word[i] + mask[i]) % len(self.letters) for i in range(len(word))]
        cipher = [self.index2letter[i] for i in cipher]
        cipher = ''.join(cipher)

        return cipher

    def decode(self, cipher):
        '''Decodes given string. Every charachter in the given word
        shifted back accourding to corresponding letters index from the mask'''

        assert len(cipher) > 0, ValueError('Empty String')

        mask = self.__get_mask(cipher)

        mask = [self.letter2index[letter] for letter in mask]
        cipher = [self.letter2index[letter] for letter in cipher]

        word = [(cipher[i] - mask[i]) % len(self.letters)  for i in range(len(cipher))]
        word = [self.index2letter[i] for i in word]
        word = ''.join(word)

        return word

    def __get_mask(self, word):
        '''Creates matching length mask from key word for any given string'''
        mask = self.key * ceil(len(word) / len(self.key))
        mask = mask[:len(word)]
        return mask
