import re


def bin2dec(value):
    VALID_BINARY_STRING = r'^[0-1]+$'

    if type(value) != str:
        raise ValueError('Invalid binary type.')

    if not re.match(VALID_BINARY_STRING, value):
        raise ValueError('Invalid binary string.')

    exponent = len(value) - 1
    result = 0
    for digit in value:
        result += int(digit) * 2 ** exponent
        exponent -= 1
    return result
