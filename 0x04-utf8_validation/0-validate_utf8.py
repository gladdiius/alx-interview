#!/usr/bin/python3
"""
0-validate_utf8.py
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    
    def is_start_byte(byte):
        """ starting byte """
        return (byte >> 6) == 0b00
    
    def is_continuation_byte(byte):
        """ continuition byte"""
        return (byte >> 6) == 0b10
    
    remaining_bytes = 0
    
    for byte in data:
        if remaining_bytes == 0:
            if is_start_byte(byte):
                if (byte >> 7) == 0:
                    continue
                elif (byte >> 5) == 0b110:
                    remaining_bytes = 1
                elif (byte >> 4) == 0b1110:
                    remaining_bytes = 2
                elif (byte >> 3) == 0b11110:
                    remaining_bytes = 3
                else:
                    return False
            else:
                return False
        else:
            if is_continuation_byte(byte):
                remaining_bytes -= 1
            else:
                return False
        
            if remaining_bytes < 0:
                return False
        
    return remaining_bytes == 0
