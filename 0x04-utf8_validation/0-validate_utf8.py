#!/usr/bin/python3
"""
This software defines rules to check if an integer combination is a valid
UTF-8 Encoding

A valid UTF-8 character can be 1 - 4 bytes long.
For a 1-byte character, the first bit is a 0, followed by its unicode.
For an n-bytes character, the first n-bits are all ones, the n+1 bit is 0,
followed by n-1 bytes with most significant 2 bits being 10.
"""


def validUTF8(data):
    """
    Data: a list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """
    byte_count = 0

    for i in data:
        if byte_count == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                byte_count = 1
            elif i >> 4 == 0b1110:
                byte_count = 2
            elif i >> 3 == 0b11110:
                byte_count = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            byte_count -= 1
    return byte_count == 0
