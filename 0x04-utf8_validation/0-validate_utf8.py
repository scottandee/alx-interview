#!/usr/bin/python3
"""utf8 Validation
"""


def validUTF8(data):
    """This script determines if a given set of
    data is valid utf8
    """
    if data == []:
        return True
    if data[0] > 128:
        # select first eight bits of supposed multibyte character
        multi_byte = int(bin(data[0])[-8:], 2)
        byte_num = 0

        # check if it's a valid multi-byte character
        if 194 <= multi_byte <= 223:
            byte_num = 2
        if 224 <= multi_byte <= 239:
            byte_num = 3
        if 240 <= multi_byte <= 244:
            byte_num = 4
        # print(multi_byte, byte_num)

        # return false if it's not a valid multi-byte character
        if byte_num == 0:
            return False
        # return false if the number of bytes specified in multi-byte
        # character is less than the number of characters
        if len(data) < byte_num:
            return False
        for d in data[1:]:
            continuation_byte = d
            if d >= 128:
                continuation_byte = int(bin(d)[-8:], 2)
            else:
                continue
            # check if it's a valid continuation-byte character
            if 128 <= continuation_byte <= 191:
                continue
            return False
        return True
    else:
        # Handle single bytes
        for d in data:
            if d > 128:
                return False
        return True
