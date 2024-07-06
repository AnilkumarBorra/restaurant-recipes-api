"""
sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding two numbers."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_sub_number(self):
        """Test subtract two numbers."""
        res = calc.subtract(10, 10)
        self.assertEqual(res, 0)
