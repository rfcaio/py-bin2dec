import unittest

from bin2dec import bin2dec


class Bin2DecTest(unittest.TestCase):
    def test_invalid_binary_type(self):
        with self.assertRaises(ValueError) as invalid_binary_type_err:
            bin2dec(101)
        self.assertEqual(
            str(invalid_binary_type_err.exception),
            'Invalid binary type.'
        )

    def test_invalid_binary_string(self):
        with self.assertRaises(ValueError) as invalid_binary_string_err:
            bin2dec('1a1')
        self.assertEqual(
            str(invalid_binary_string_err.exception),
            'Invalid binary string.'
        )

    def test_bin2dec(self):
        self.assertEqual(bin2dec('101111'), 47)
        self.assertEqual(bin2dec('10111100'), 188)
