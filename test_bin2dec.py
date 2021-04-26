import unittest

from bin2dec import bin2dec


class Bin2DecTest(unittest.TestCase):
    def test_bin2dec(self):
        self.assertEqual(bin2dec('101111'), 47)
        self.assertEqual(bin2dec('10111100'), 188)

        with self.assertRaises(ValueError):
            bin2dec('1a1')
