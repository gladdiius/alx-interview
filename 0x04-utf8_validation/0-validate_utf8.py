#!/usr/bin/python3
"""0-validate_utf8"""


def validUTF8(data):
    """
    Check if a given data set represents a valid UTF-8 encoding.

    Args:
    data: A list of integers representing the data bytes

    Returns:
    True if data is a valid UTF-8 encoding, else False
    """

    bytes_to_follow = 0

    for byte in data:
        if bytes_to_follow == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                bytes_to_follow = 1
            elif byte >> 4 == 0b1110:
                bytes_to_follow = 2
            elif byte >> 3 == 0b11110:
                bytes_to_follow = 3
            else:
                return False

        else:
            if byte >> 6 != 0b10:
                return False
            bytes_to_follow -= 1

        if bytes_to_follow > len(data) - 1 - data.index(byte):
            return False

    return bytes_to_follow == 0
