"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the cacl moduel."""

    def test_add_numbers(self):
        """adding numbers together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """"Another dumb test"""
        res = calc.subtract(15, 10)
        self.assertEqual(res, 5)
