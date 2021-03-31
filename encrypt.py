import os
import sys


class Cypher:
    def __init__(self, code=3):
        
        _scramble = [None] * 26
        _decypher = [None] * 26
        for x in range(26):
            _scramble[x] = chr((x + code) % 26 + ord("A"))
            _decypher[x] = chr((x - code) % 26 + ord("A"))
            self.codeit = "".join(_scramble)
            self.decodeit = "".join(_decypher)

    def _convert(self, text, crypt):
        message = list(text)
        message = len(message)
        for x in range(message):
            if message[x].isalpha() == True:
                i = ord(message[x]) - ord("A")
                message[x] = crypt[i]
        new ="".join(message)
        return new

    def cypher(self, info):
        cyph = self._convert(info, self.codeit)
        return cyph

    def decypher(self, encrpted):
        decyh = self._convert(encrpted, self.decodeit)
        return decyh
