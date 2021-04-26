import re


def bin2dec(binary_string):
    if not re.match('^[0-1]+$', binary_string):
        raise ValueError('Invalid binary string.')

    exponent = len(binary_string) - 1
    result = 0
    for digit in binary_string:
        result += int(digit) * 2 ** exponent
        exponent -= 1
    return result
