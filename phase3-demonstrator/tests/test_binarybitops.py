import argparse
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from binarybitops import calculate_operations, parse_operand


class BinaryBitOpsTests(unittest.TestCase):
    def test_default_example_results(self):
        self.assertEqual(calculate_operations(12, 10), {"AND": 8, "OR": 14, "XOR": 6})

    def test_parses_decimal_hex_and_binary(self):
        self.assertEqual(parse_operand("12"), 12)
        self.assertEqual(parse_operand("0xC"), 12)
        self.assertEqual(parse_operand("0b1100"), 12)

    def test_accepts_unsigned_16_bit_boundaries(self):
        self.assertEqual(parse_operand("0"), 0)
        self.assertEqual(parse_operand("65535"), 65535)

    def test_rejects_values_outside_16_bit_range(self):
        for value in ("-1", "65536"):
            with self.subTest(value=value), self.assertRaises(argparse.ArgumentTypeError):
                parse_operand(value)


if __name__ == "__main__":
    unittest.main()
