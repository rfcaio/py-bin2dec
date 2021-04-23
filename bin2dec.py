def bin2dec(binary_string):
    exponent = len(binary_string) - 1
    result = 0
    for digit in binary_string:
        result += int(digit) * 2 ** exponent
        exponent -= 1
    return result
